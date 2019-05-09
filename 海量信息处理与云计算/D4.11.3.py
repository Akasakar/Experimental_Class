# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: D4.11.3.py
# Created:  2019.05.09(UTC+0800)19.47.44(星期四)
'''

def load_data(datalog):
    dataset, idmap, idset = [], {}, set()
    for dl in datalog:
        a = ()
        for di in dl:
            if di not in idset:
                idset.add(di)
                idmap[di] = len(idset)
            a += (idmap[di],)
        dataset.append(a)
    return dataset, dict(zip(idmap.values(), idmap.keys()))

def has_infrequent_subset(c, L):
    for i in range(len(c)):
        tmp = c[:i] + c[i + 1:]
        if tmp not in L:
            return True
    return False

def apriori_gen(L, min_sup):
    Ck, cset =[], set()
    for l1 in L:
        for l2 in L:
            ok = (l1[-1] != l2[-1])
            for i in range(len(l1) - 1):
                if ok and l1[i] != l2[i]:
                    ok = False
            if ok:
                ls = list(l1)
                ls.sort()
                l1 = tuple(ls)
                c = l1 + (l2[-1],)
                if c in cset or has_infrequent_subset(c, set(L)):
                    del c
                else:
                    cset.add(c)
                    Ck.append(c)
    return Ck

def apriori(D, vmap, min_sup, min_conf):
    L1, cnt1, idset, lenD = [], {}, set(), len(D)
    for ds in D:
        for di in ds:
            if di not in idset:
                idset.add(di)
                cnt1[(di,)] = 0
            cnt1[(di,)] += 1
    for k, v in cnt1.items():
        if v >= lenD * min_sup:
            L1.append(k)

    for k in range(2, len(idset)):
        if L1 == []:
            break
        Ck, L2, cnt2 = apriori_gen(L1, min_sup), [], {}
        for t in Ck:
            cnt2[t] = 0
            for d in D:
                if set(t).issubset(set(d)):
                    cnt2[t] += 1
        for t in Ck:
            if cnt2[t] >= lenD * min_sup:
                L2.append(t)
                if cnt2[t] / cnt1[t[:-1]] >= min_conf:
                    s = "(" + vmap[t[0]]
                    for i in range(1, len(t) - 1):
                        s += "," + vmap[t[i]]
                    s += ") ==> ({0}) conf({1})".format(vmap[t[-1]], round(cnt2[t] / cnt1[t[:-1]], 3))
                    print(s)

        L1 = L2.copy()
        cnt1 = cnt2.copy()


def main():
    datalog = (
            ("面包", "甜酱", "芝麻酱"),
            ("面包", "芝麻酱"),
            ("面包", "芝麻酱", "牛奶"),
            ("面包", "啤酒"),
            ("牛奶", "啤酒")
            )
    dataset, vmap= load_data(datalog)
    apriori(dataset, vmap, 0.2, 0.2)

if __name__ == "__main__":
    main()
