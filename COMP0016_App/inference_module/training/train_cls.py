import argparse
import os
import random
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.optim as optim
import torch.utils.data
import torch.nn.functional as F
import torch.nn
from tqdm import tqdm
from model.dataset import JawDataset
from model.model import PointNetReg, feature_transform_regularizer

NUM_POINTS = 2048
BATCH_SIZE = 12

parser = argparse.ArgumentParser()
parser.add_argument(
    '--batchSize', type=int, default=12, help='input batch size')
parser.add_argument(
    '--num_points', type=int, default=2048, help='input batch size')
parser.add_argument(
    '--nepoch', type=int, default=50, help='number of epochs to train for')
parser.add_argument('--outf', type=str, default='cls', help='output folder')
parser.add_argument('--model', type=str, default='', help='model path')
parser.add_argument('--dataset', type=str, required=True, help="dataset path")
parser.add_argument('--feature_transform', default=True, help="use feature transform")

opt = parser.parse_args(['--dataset', 'drive/MyDrive/Tooth_Wear_Deep_Learning/PLY_dataset'])
print(opt)


blue = lambda x: '\033[94m' + x + '\033[0m'

opt.manualSeed = random.randint(1, 10000)  # fix seed
print("Random Seed: ", opt.manualSeed)
random.seed(opt.manualSeed)
torch.manual_seed(opt.manualSeed)

dataset = JawDataset(root=opt.dataset, npoints=opt.num_points, split='train')
test_dataset = JawDataset(root=opt.dataset, split='test', npoints=opt.num_points, data_augmentation=False)

dataloader = torch.utils.data.DataLoader(
    dataset,
    batch_size=opt.batchSize,
    shuffle=True)

testdataloader = torch.utils.data.DataLoader(
        test_dataset,
        batch_size=opt.batchSize,
        shuffle=True)


classifier = PointNetReg(feature_transform=opt.feature_transform)

if opt.model != '':
    classifier.load_state_dict(torch.load(opt.model))


optimizer = optim.Adam(classifier.parameters(), lr=0.001, betas=(0.9, 0.999))
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=20, gamma=0.5)
classifier.cuda()

num_batch = len(dataset) / opt.batchSize

for epoch in range(opt.nepoch):
    scheduler.step()
    for i, data in enumerate(dataloader):
        points, target = data
        # target = target[:, 0]
        # print("target", target)
        points = points.transpose(2, 1)
        points, target = points.cuda(), target.cuda()
        optimizer.zero_grad()
        classifier = classifier.train()
        pred, trans, trans_feat = classifier(points)
        # print("pred: ", pred)

        L = nn.MSELoss()
        loss = L(pred, target)
        if opt.feature_transform:
            loss += feature_transform_regularizer(trans_feat) * 0.001
        loss.backward()
        optimizer.step()
        pred_choice = pred.data
        out = torch.where(pred_choice < 0.5, 0, pred_choice)
        out = torch.where((out >= 0.5) & (out < 1.5), 1, out)
        out = torch.where((out >= 1.5) & (out < 2.5), 2, out)
        out = torch.where((out >= 2.5) & (out < 3.5), 3, out)
        out = torch.where((out >= 3.5) & (out <= 4.5), 4, out)
        correct = out.eq(target.data).cpu().sum()
        print('[%d: %d/%d] train loss: %f accuracy: %f' % (epoch, i, num_batch, loss.item(), correct.item() / float(opt.batchSize)))
    torch.save(classifier.state_dict(), '%s/cls_model_%d.pth' % (opt.outf, epoch))

total_correct = 0
total_testset = 0
for i,data in tqdm(enumerate(testdataloader, 0)):
    points, target = data
    # target = target[:, 0]
    points = points.transpose(2, 1)
    points, target = points.cuda(), target.cuda()
    classifier = classifier.eval()
    pred, _, _ = classifier(points)
    pred_choice = pred.data
    out = torch.where(pred_choice < 0.5, 0, pred_choice)
    out = torch.where((out >= 0.5) & (out < 1.5), 1, out)
    out = torch.where((out >= 1.5) & (out < 2.5), 2, out)
    out = torch.where((out >= 2.5) & (out < 3.5), 3, out)
    out = torch.where(out >= 3.5, 4, out)
    correct = out.eq(target.data).cpu().sum()
    total_correct += correct.item()
    total_testset += points.size()[0]

print("final accuracy {}".format(total_correct / float(total_testset)))