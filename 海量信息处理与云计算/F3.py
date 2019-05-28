# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: F3.py
# Created:  2019.05.28(UTC+0800)14.22.31(星期二)
'''

import pandas
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy  #用于进行层次聚类，话层次聚类图的工具包

def main():
    df = [[0,4,6,1,6],[4,0,9,7,3],[6,9,0,10,5],[1,7,10,0,8],[6,3,5,8,0]]
    Z = hierarchy.linkage(df, method ='single', metric='euclidean')
    tmp = hierarchy.dendrogram(Z)
    plt.show()

if __name__ == "__main__":
    main()
