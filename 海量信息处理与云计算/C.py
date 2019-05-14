# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: C.py
# Created:  2019.05.11(UTC+0800)20.42.58(星期六)
'''

from pyecharts import options as opts
from pyecharts.charts import Page, Radar, Parallel
from pyecharts.globals import ThemeType
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import parallel_coordinates

def radar_base(data) -> Radar:
    c = (
        Radar(opts.InitOpts(width = "1200px", height = "800px"))
        .add_schema (
            schema = [
                opts.RadarIndicatorItem(name="Murder", max_ = 30),
                opts.RadarIndicatorItem(name="Forcible rape", max_= 50),
                opts.RadarIndicatorItem(name="Robbery", max_= 300),
                opts.RadarIndicatorItem(name="Aggravated assault", max_= 5000),
                opts.RadarIndicatorItem(name="Burglary", max_= 1000),
                opts.RadarIndicatorItem(name="Larceny thief", max_= 3000),
                opts.RadarIndicatorItem(name="Motor Vehicle theft", max_= 1000),
            ]
        )
        .set_series_opts(label_opts = opts.LabelOpts(is_show = False))
        .set_global_opts (
            title_opts = opts.TitleOpts(title = "美国各州犯罪率"),
            legend_opts = opts.LegendOpts(type_ = 'scroll', selected_mode = 'single', pos_top = "5%"),
            toolbox_opts = opts.ToolboxOpts()
            )
    )
    for i in range(len(data)):
        c.add(data[i][0], [list(map(float, data[i][1:]))])
    return c

def parallel_base(dataSet) -> Parallel:
    nameSet, data = set(), {}
    for ds in dataSet:
        if ds[-1] not in nameSet:
            nameSet.add(ds[-1])
            data[ds[-1]] = []
        data[ds[-1]].append(list(map(float, ds[:-1])))

    c = (
        Parallel(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add_schema(
            [
                {"dim": 0, "name": "calyx length"},
                {"dim": 1, "name": "calyx width"},
                {"dim": 2, "name": "petal length"},
                {"dim": 3, "name": "petal width"},
            ]
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="鸢尾花数据集"))
    )
    for k in data.keys():
        c.add(k, data[k])
    return c

def Ex3_6_7():
    D = np.array([
        [0, 125, 1239, 3026, 480, 3300, 3736, 1192, 2373, 1230],
        [125, 0, 1150, 1954, 604, 3330, 3740, 1316, 2389, 1207],
        [1239, 1150, 0, 1945, 1717, 3929, 4157, 2092, 1892, 2342],
        [3026, 1954, 1945, 0, 1847, 3202, 2457, 1570, 993, 3156],
        [480, 604, 1717, 1847, 0, 2825, 3260, 716, 2657, 1710],
        [3300, 3330, 3929, 3202, 2825, 0, 2668, 2111, 4279, 4531],
        [3736, 3740, 4157, 2457, 3260, 2668, 0, 2547, 3431, 4967],
        [1192, 1316, 2092, 1570, 716, 2111, 2547, 0, 2673, 2422],
        [2373, 2389, 1892, 993, 2657, 4279, 3431, 2673, 0, 3592],
        [1230, 1207, 2342, 3156, 1710, 4531, 4967, 2422, 3592, 0]
    ])
    n = len(D)
    A = np.zeros((n, n))
    sumD = np.sum(np.multiply(D, D)) / n ** 2
    sumrD = [np.sum(np.multiply(D[i, ...], D[i, ...])) / n for i in range(n)]
    sumcD = [np.sum(np.multiply(D[..., j], D[..., j])) / n for j in range(n)]
    for i in range(n):
        for j in range(n):
            A[i][j] = (-D[i][j] ** 2 + sumrD[i] + sumcD[j] - sumD) / 2
    W, V = np.linalg.eig(A)
    X, Y = np.zeros(n), np.zeros(n)
    for i in range(n):
        X[i], Y[i] = V[i][0] * np.sqrt(W[0]), V[i][1] * np.sqrt(W[1])
    plt.scatter(X, Y)
    plt.axis([-3000, 3000, -3000, 3000])
    plt.show()
    

if __name__ == "__main__":
    #美国各州犯罪率
    data = pd.read_csv("美国各州犯罪率.csv").values.tolist()
    #雷达图
    radar_base(data).render("美国各州犯罪率Radar.html")

    #鸢尾花数据集
    iris = pd.read_csv('鸢尾花数据.csv')
    #散点矩阵图
    sns.pairplot(iris, hue = 'species',)
    plt.show()
    #平行坐标图
    '''
    _, axes = plt.subplots()
    parallel_coordinates(iris, 'species',ax = axes)
    plt.show()
    '''
    parallel_base(iris.values.tolist()).render("鸢尾花数据parallel.html")

    #城市距离相对位置关系，MDS分析
    Ex3_6_7()
