# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: F1.py
# Created:  2019.05.25(UTC+0800)21.06.33(星期六)
'''

import pandas
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy  #用于进行层次聚类，话层次聚类图的工具包

def main():
    df = pandas.read_excel("国民经济发展指标数据.xlsx", index_col = 0)
    Z = hierarchy.linkage(df, method ='average', metric='euclidean')
    tmp = hierarchy.dendrogram(Z, labels = df.index)
    plt.title("层次聚类")
    plt.show()

if __name__ == "__main__":
    main()
