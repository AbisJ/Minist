from re import M
from turtle import shape
import numpy as np

X = np.random.normal(size=(3, 1))
W_xh = np.random.normal(size=(1, 4))
H = np.random.normal(size=(3, 4))
W_hh = np.random.normal(size=(4, 4))

A = np.dot(X, W_xh)
if A.shape == H.shape:
    print(True)


J = np.dot(H, W_hh) + A
x1= np.c_[X, H]
print (x1.shape)
w1 = np.r_[W_xh, W_hh]
print(w1.shape)
M = np.dot(x1, w1)
if J.all() == M.all():
    print (True)