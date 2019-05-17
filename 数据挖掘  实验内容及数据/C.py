# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: C.py
# Created:  2019.05.16(UTC+0800)18.08.24(星期四)
'''

import math

#分类所需期望
def Except(data):
    cnt = {'NO':0, 'YES':0}
    for dr in data:
        cnt[dr[-1]] += 1
    if cnt['NO'] * cnt['YES'] == 0:
        return 0
    else:
        return sum([-v / len(data) * math.log(v / len(data), 2) for v in cnt.values()])

def EAf(data, idset, attribute, k):
    cnt = {}
    for dr in data:
        cnt[dr[k]] = []
    for dr in data:
        cnt[dr[k]].append(dr)
    return sum([len(v) / len(data) * Except(v) for v in cnt.values()])

def Gain(data, idset, attribute, k):
    return Except(data) - EAf(data, idset, attribute, k)

def MaxGain(data, idset, attribute, col):
    k, mg = 0, 0
    for i in range(len(idset) - 1):
        if col[i]:
            continue
        tmp = Gain(data, idset, attribute, i)
        if tmp > mg:
            mg = tmp
            k = i
    return k

def ID3(data, idset, attribute, col):
    k = MaxGain(data, idset, attribute, col)
    #初始化
    cnt = {}
    for dr in data:
        cnt[dr[k]] = []
    #同类型返回
    if len(cnt)  == 1:
        return data[0][-1]
    #按属性k分类
    for dr in data:
        cnt[dr[k]].append(dr)
    col[k] = True
    return {idset[k]:{key:ID3(v, idset, attribute, col.copy()) for key, v in cnt.items()}}

def Check(tree, data, idset):
    att = {idset[i]:i for i in range(len(idset))}
    mat = [[0,0],[0,0]]
    rk = list(tree.keys())[0]
    for dr in data:
        root = tree[rk]
        ks = rk
        while True:
            if dr[att[ks]] not in set(root.keys()):
                mat[dr[-1] == 'YES'][0] += 1
                break
            root = root[dr[att[ks]]]
            if type(root) != type(dict()):
                mat[dr[-1] == 'YES'][root == 'YES'] += 1
                break
            ks = list(root.keys())[0]
            root = root[ks]
    print("Confusion Matrix")
    for m in mat:
        print(m)

def main():
    print("Hello py")
    rL = []
    with open("实验3-bank-data.csv", "r") as f:
        rL = f.read().split('\n')[3:-1]
    idset = [rL[i].split()[1] for i in range(11)]
    attribute = {
            'age':('age<=41', 'age>41'),
            'sex':('FEMALE', 'MALE'),
            'region':('INNER_CITY','TOWN','RURAL','SUBURBAN'),
            'income':('income<=15538.8', '15538.8<income<=21506.2', '21506.2<age<=30189.4', '30189.4<age<=44288.3', 'age>44288.3'),
            'married':('NO','YES'),
            'children':('0', '1', '2', '3'),
            'car':('NO', 'YES'),
            'save_act':('NO','YES'),
            'current_act':('NO','YES'),
            'mortgage':('NO','YES'),
            'pep':('NO','YES')
            }
    data = [dr.split(',')[1:] for dr in rL[13:]]
    #离散化一下
    for i in range(len(data)):
        data[i][0] = attribute['age'][int(data[i][0]) > 41]
        tmp = float(data[i][3])
        k = (tmp > 15538.8) + (tmp > 21506.2) + (tmp > 30189.4) + (tmp > 44288.3)
        data[i][3] = attribute['income'][k]
        #data[i][5] = int(data[i][5])
    #前2/3拿去训练出分类
    tree = ID3(data[:len(data) // 3 * 2], idset, attribute, [False for i in range(len(idset))])
    print(tree)
    #后1/3拿去测试
    Check(tree, data[len(data) // 3 * 2:], idset)

if __name__ == "__main__":
    main()
