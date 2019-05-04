# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: B.py
# Created:  2019.05.04(UTC+0800)17.22.48(星期六)
'''

def readFile(ds, idSet, idMap):
    rL = []
    with open("实验2-Groceries.csv", "r") as f:
        rL = f.read().split("\n")[1:-1]
    for r in rL:
        a = tuple(map(str.strip, r[r.find("{") + 1 : r.rfind("}")].split(",")))
        b = []
        for c in a:
            if c not in idSet:
                idSet.add(c)
                idMap[c] = len(idSet)
            b.append(idMap[c])
        b.sort()
        ds.append(tuple(b))

def writeFile(a, c, vMap):
    s = "(" + vMap[a[0]]
    for i in range(1, len(a) - 1):
        s += "," + vMap[a[i]]
    s += ") ==> (" + vMap[a[-1]] + ") conf({0})\n".format(c)
    with open("Groceries.dat", "a") as f:
        f.write(s)

def find_frequent_1_itemsets(D, min_sup):
    cnt = {}
    for t in D:
        for v in t:
            cnt[v] = 0
    for t in D:
        for v in t:
            cnt[v] += 1
    L1 = []
    n = len(D)
    for k, v in cnt.items():
        if v >= n * min_sup:
            L1.append((k,))
    return L1

def has_infrequent_subset(c, setL):
    for i in range(len(c)):
        s = c[:i] + c[i + 1:]
        if s not in setL:
            return True
    return False

def apriori_gen(L, lenK, min_sup):
    Ck = []
    for l1 in L:
        for l2 in L:
            ok = (l1[-1] != l2[-1])
            for k in range(lenK - 1):
                if ok and l1[k] != l2[k]:
                    ok = False
            if ok:
                c = l1 + (l2[-1],)
                if has_infrequent_subset(c, set(L)):
                    del c
                else:
                    Ck.append(c)
    return Ck

def cntSet(dataSet, L):
    tMap = {}
    for t in L:
        tMap[t] = 0
        for ds in dataSet:
            if set(t).issubset(set(ds)):
                tMap[t] += 1
    return tMap

def apriori(dataSet, min_sup, min_conf, vMap):
    L1 = find_frequent_1_itemsets(dataSet, min_sup)
    t1Map = cntSet(dataSet, L1)
    kn = len(L1)
    n = len(dataSet)
    for k in range(2, kn):
        if L1 == []:
            break;
        Ck = apriori_gen(L1, k - 1, min_sup)
        L2 = []
        t2Map = cntSet(dataSet, Ck)
        for t in Ck:
            if t2Map[t] >= n * min_sup:
                L2.append(t)
                conf = t2Map[t] / t1Map[t[:-1]]
                if conf >= min_conf:
                    writeFile(t, conf, vMap)
        L1 = L2.copy()
        t1Map = t2Map.copy()

def main():
    dataSet, idSet, idMap, vMap = [], set(), {}, {}
    readFile(dataSet, idSet, idMap)
    vMap = dict(zip(idMap.values(), idMap.keys()))
    apriori(dataSet, 0.01, 0.5, vMap)

if __name__ == "__main__":
    main()
