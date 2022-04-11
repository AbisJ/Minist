from msilib.schema import FeatureComponents
import torch
import math
import torch.nn as nn
from torch.nn import functional as F
import matplotlib.pyplot as plt
import pandas as pd



print(torch.cuda.is_available())

# x = F.one_hot(torch.tensor([0,2]), 8)
# print(x)
'''小批量数据形状，（批量大小，时间步数）'''
X = torch.arange(10).reshape(2,5)
print(X)
Y = F.one_hot(X.T, 20).cuda()
print(Y.shape)
78