import numpy as np
import torch
from plyfile import PlyData
from model.model import PointNetReg

N_POINTS = 2048

def get_prediction(plydata):
    # Load the trained model 
    model = PointNetReg(feature_transform = False)
    model.load_state_dict(torch.load('trained_models/cls_model_49.pth', map_location=torch.device('cpu')))

    pts = np.vstack([plydata['vertex']['x'], plydata['vertex']['y'], plydata['vertex']['z']]).T
    choice = np.random.choice(len(pts), N_POINTS, replace=True)
    point_set = pts[choice, :]

    point_set = point_set - np.expand_dims(np.mean(point_set, axis=0), 0)
    dist = np.max(np.sqrt(np.sum(point_set ** 2, axis=1)), 0)
    points = point_set / dist
    points = torch.from_numpy(points).float()
    points = points.unsqueeze(0)
    points = points.transpose(2, 1)

    # Predict
    model.eval()
    pred, _, _ = model(points)
    pred_choice = pred.data
    label = pred_choice.cpu().numpy()[0][0]
    if label < 0.5:
        label = 0
    elif label >= 0.5 and label < 1.5:
        label = 1 
    elif label >= 1.5 and label < 2.5:
        label = 2
    elif label >= 2.5 and label < 3.5:
        label = 3
    elif label >= 3.5 and label < 4.5:
        label = 4

    return label
