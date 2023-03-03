import os
import open3d as o3d
import glob
import numpy as np
import torch.utils.data as data
import os.path
import torch
from tqdm import tqdm 
from plyfile import PlyData, PlyElement

input_file = 'COMP0016_App/inference_module/model/All_teeth'

class JawDataset(data.Dataset):
    def __init__(self,
                 root=input_file,
                 npoints=2048,
                 split='train',
                 data_augmentation=True):
        self.npoints = npoints
        self.root = root
        self.split = split
        self.data_augmentation = data_augmentation

        self.point = []
        self.labels = []

        self.files = glob.glob(os.path.join(input_file, "All_teeth/{}/inputs/*".format(self.split)))
        # self.test_files = glob.glob(os.path.join(input_file, "test/inputs/*"))
  
    
        # for f in self.files:
        #     print("processing: {}".format(os.path.basename(f)))
        #     self.point.append(trimesh.load(f).sample(self.npoints))
        path = os.path.join(input_file, 'All_teeth/{}/labels/label.txt'.format(self.split))
        

        with open(path) as f:
            for line in f:
                ls = line.strip()
                # lb = [int(x) for x in ls]
                self.labels.append(ls)


    def __getitem__(self, index):
        file = self.files[index]
        label = self.labels[index]
        with open(file, 'rb') as f:
            plydata = PlyData.read(f)
        pts = np.vstack([plydata['vertex']['x'], plydata['vertex']['y'], plydata['vertex']['z']]).T
        choice = np.random.choice(len(pts), self.npoints, replace=True) # why use true here
        point_set = pts[choice, :]

        point_set = point_set - np.expand_dims(np.mean(point_set, axis=0), 0)  # center
        dist = np.max(np.sqrt(np.sum(point_set ** 2, axis=1)), 0)
        point_set = point_set / dist  # scale

        if self.data_augmentation:
            theta = np.random.uniform(0, np.pi * 2)
            rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
            point_set[:, [0, 2]] = point_set[:, [0, 2]].dot(rotation_matrix)  # random rotation
            point_set += np.random.normal(0, 0.02, size=point_set.shape)  # random jitter

        point_set = torch.from_numpy(point_set.astype(np.float32))
        label = torch.from_numpy(np.array([label]).astype((np.float32)))
        return point_set, label


    def __len__(self):
        return len(self.files)
    

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import pytorch3d
    from pytorch3d.structures import Pointclouds

    d = JawDataset(input_file)
    print(len(d))
    print(d[0][0], d[0][1])
    print(d[0][0].dim())
    
    print(d[0][0])
    print(d[0][0].shape)

    pc = Pointclouds([d[0][0]])
    np_points = pc.points_packed().detach().numpy()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(np_points[:, 0], np_points[:, 1], np_points[:, 2])
    plt.show()