# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: E.py
# Created:  2019.05.24(UTC+0800)10.22.37(星期五)
'''


import pandas
import random

def Kmeans(data, k):
    p, ans, eps= [[],random.sample(data, k)], {}, 1e-3
    while True:
        p[0] = p[1].copy()
        mp = {i:[] for i in range(k)}
        for dr in data:
            i, pos, dis = 0, 0, 1e9
            for pr in p[1]:
                tmp = (dr[0] - pr[0]) ** 2 + (dr[1] - pr[1]) ** 2
                if dis - tmp > eps:
                    pos = i
                    dis = tmp
                i += 1
            mp[pos].append(dr)
        for i in range(k):
            if len(mp[i]) == 0:
                    continue
            sumx, sumy = 0, 0
            for dr in mp[i]:
                sumx += dr[0]
                sumy += dr[1]
            p[1][i] = [sumx / len(mp[i]), sumy / len(mp[i])]
        if sum([abs(p[0][i][0] - p[1][i][0]) < eps and abs(p[0][i][1] - p[1][i][1]) < eps for i in range(k)]) >= k:
            ans = mp.copy()
            break
    return ans, p[1]

def main():
    data = pandas.read_csv("实验5-iris.txt", header = None).values.tolist()
    mp, p = Kmeans([dr[:-1] for dr in data], 3)
    ciris = []
    for pr in p:
        i, pos, dis = 0, 0, 1e9
        for dr in data:
            tmp = (pr[0] - dr[0]) ** 2 + (pr[1] - dr[1]) ** 2
            if dis - tmp > 1e-3:
                dis = tmp
                pos = i
            i += 1
        ciris.append(data[pos][-1])
    for k, v in mp.items():
        cnt = {False:0, True:0}
        for vr in v:
            for dr in data:
                if vr[0] == dr[0] and vr[1] == dr[1]:
                    s = "Expect({0}) ForeCast({1}) ==> {2}"
                    print(vr, s.format(dr[-1][5:], ciris[k][5:], ["Wa", "Ac"][ciris[k] == dr[-1]]))
                    cnt[ciris[k] == dr[-1]] += 1
        print("class", ciris[k], cnt)
        print("------------------------------------------")

if __name__ == "__main__":
    main()
