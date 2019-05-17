# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: D.py
# Created:  2019.05.16(UTC+0800)12.36.00(星期四)
'''

import pandas

def KNN(Train, Test, k):
    for t in Test:
        tmp = sorted([((x[0] - t[0]) ** 2 + (x[1] - t[1]) ** 2, x[2]) for x in Train])
        cnt, idset = {}, set()
        for i in range(0, min(k, len(tmp))):
            if tmp[i][1] not in idset:
                idset.add(tmp[i][1])
                cnt[tmp[i][1]] = 0
            cnt[tmp[i][1]] += 1
        print(t[0], t[1], "type", sorted(cnt)[-1])


if __name__ == "__main__":
    Train = pandas.read_csv("实验4-KNN数据集(已知).txt", header = None).values.tolist()
    Test = pandas.read_csv("实验4-KNN数据集(未知).txt", header = None).values.tolist()
    KNN(Train, Test, 10)
