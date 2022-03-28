# 导入相关模块
import json
import matplotlib
import matplotlib.pyplot as plt
import os

import numpy as np


def plot_binomial(sample,sample2):
    '''绘制二项分布的概率质量函数'''
    #sample = [0.1,0.11,0.13,-0.12,-0.14,-0.17,-0.2,-0.23,-0.33,-0.35,0.01,-0.35,0.2,0.22,0.23,0.13,0.14]
    #sample2 = [-0.1, -0.11, 0.13, -0.12, -0.14, 0.17, 0.2, 0.23, 0.33, 0.35, 0.01, 0.35, 0.2, 0.22, 0.23, 0.13, 0.14]
    print(sample)
    plt.hist(sample, bins=20, range=[-0.3, 0.3], alpha=0.5, label='left',rwidth=0.5)  # 绘制直方图
    plt.hist(sample2, bins=20, range=[-0.3, 0.3], alpha=0.5, label='right',rwidth=0.5)  # 绘制直方图
    plt.legend(loc='upper right')
    plt.show()

rootpath = "H:\\TestData\\FitWithVTK"
left = []
right = []
for root, dirs, files in os.walk(rootpath, topdown=False):
    for name in dirs:
        #print(os.path.join(root, name))
        print()
        with open(rootpath + "\\" + name +"\\" + name[0:8] + "-result.json", 'r') as f:
            temp = json.loads(f.read())
            left.append(float(temp['leftLength']))
            right.append(float(temp['rightLength']))
print("left: average->%f ,median->%f, variance->%f"%(np.average(left),np.median(left),np.var(left)))
print("right: average->%f ,median->%f, variance->%f"%(np.average(right),np.median(right),np.var(right)))
plot_binomial(left,right)

