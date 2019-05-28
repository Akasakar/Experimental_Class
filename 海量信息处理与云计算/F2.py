# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: F2.py
# Created:  2019.05.27(UTC+0800)22.06.53(星期一)
'''

import random

def Kmeans(data, k):
    p, eps = random.sample(data, k), 1e-3
    while True:
        q, mp = p.copy(), {i:[] for i in range(k)}
        # 划分点
        for dr in data:
            pos, dis = 0, 1e18
            for i in range(len(q)):
                tmp = sum([(dr[j] - q[i][j]) ** 2 for j in range(len(dr))])
                if dis > tmp:
                    dis, pos = tmp, i
            mp[pos].append(dr)
        # 计算中心点
        for i in range(k):
            if len(mp[i]) == 0:
                continue
            sump = [0.0 for j in range(len(mp[i][0]))]
            for dr in mp[i]:
                for j in range(len(dr)):
                    sump[j] += dr[j]
            p[i] = [sp / len(mp[i]) for sp in sump]
        # 判稳定性
        cnt = 0
        for i in range(k):
            for j in range(len(p[i])):
                cnt += abs(p[i][j] - q[i][j]) < eps
        if cnt >= k * len(p[0]):
            return mp
    return {}

import pandas
import numpy
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import tkinter
import tkinter.messagebox

def startKmeans(filePath, features, objects):
    try:
        data = pandas.read_excel(filePath, sheetname = [0, 1],index_col = 0)
    except Exception as e:
        tkinter.messagebox.showinfo(filePath, e)
        return
    pca = PCA(n_components = 2)
    pcamp = [pca.fit_transform(data[0].values.tolist()).tolist(), 
            pca.fit_transform(data[1].values.tolist()).tolist()]
    try:
        k = int(features)
        k = min(max(1, k), len(pcamp[0]), len(pcamp[1]))
    except Exception as e:
        tkinter.messagebox.showinfo(features, e)
        return
    try:
        objects = int(objects)
        objects = min(max(k, objects), len(pcamp[0]), len(pcamp[1]))
    except Exception as e:
        tkinter.messagebox.showinfo(objects, e)
        return

    mp = [Kmeans(pcamp[0][:objects], k),
            Kmeans(pcamp[1][:objects], k)
            ]
    color = ["red", "green", "blue", "yellow", "black", "cadetblue", "purple"]
    marker = ["o", "v", "s", "p", "h", "+", "*", "8"]
    title = ["2007", "2013"]
    for i in range(len(mp)):
        plt.subplot(len(mp), len(mp), (i + 1) ** 2)
        plt.title(title[i % 2])
        for dr in mp[i].values():
            x = numpy.array(dr)
            plt.scatter(x[:, 0], x[:, 1], marker = marker[random.randint(0, len(marker) - 1)], c = color[random.randint(0, len(color) - 1)], s = 40)
    plt.show()


def main():
    root = tkinter.Tk()
    root.title("K-means算法")
    root.geometry("300x150")
    strPath, strFea, strObj = [tkinter.StringVar() for i in range(3)]
    strPath.set("2007和2013居民消费数据.xlsx")

    tkinter.Label(root, text = "选择数据集:").place(x = 10, y = 10)
    tkinter.Label(root, text = "特征个数:").place(x = 10, y = 40)
    tkinter.Label(root, text = "对象个数:").place(x = 10, y = 70)

    tkinter.Entry(root, textvariable = strPath, width = 24).place(x = 90, y = 10)
    tkinter.Entry(root, textvariable = strFea, width = 24).place(x = 90, y = 40)
    tkinter.Entry(root, textvariable = strObj, width = 24).place(x = 90, y = 70)

    tkinter.Button(root, text = "开始聚类", command = lambda: startKmeans(strPath.get(), strFea.get(), strObj.get())).place(x = 10, y = 110)
    tkinter.Button(root, text = "退出", command = root.quit).place(x = 230, y = 110)

    root.mainloop()

if __name__ == "__main__":
    main()
