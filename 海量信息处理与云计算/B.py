# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: B.py
# Created:  2019.04.26(UTC+0800)19.56.40(星期五)
'''

import sys
import math
import pprint

def Euclidean_distance(a, b):
    ans = 0
    for i in range(len(a)):
        ans += (a[i] - b[i]) ** 2
    return math.sqrt(ans)

def Manhattan_distance(a, b):
    ans = 0
    for i in range(len(a)):
        ans += abs(a[i] - b[i])
    return ans

def Chebyshev_distance(a, b):
    ans = 0
    for i in range(len(a)):
        ans = max(ans, abs(a[i] - b[i]))
    return ans

def Minkowski_distance(a, b, k):
    if k == 1:
        return Manhattan_distance(a, b)
    else:
        return Euclidean_distance(a, b)

def dot(a, b):
    ans = 0
    for i in range(len(a)):
        ans += a[i] * b[i]
    return ans

def cosine_similarity(a, b):
    return dot(a, b) / math.sqrt(dot(a, a)) / math.sqrt(dot(b, b))

def cos_sim_Euc_dis(a, b):
    print(a, "and", b)
    print("余弦相似度:\t", cosine_similarity(a, b))
    print("欧几里得距离:\t", Euclidean_distance(a, b))

def Euc_Man_Che(a, b):
    print(a, "and", b)
    print("欧几里得距离:\t", Euclidean_distance(a, b))
    print("曼哈顿距离:\t", Manhattan_distance(a, b))
    print("切比雪夫距离:\t", Chebyshev_distance(a, b))

def Euc_Man_Che_Min(p):
    for i in range(len(p)):
        Euc_Man_Che(p[i], p[(i + 1) % 3])
        print("闵可夫斯基距离:\t",Minkowski_distance(p[i], p[(i + 1) % 3], 2))

def MinMaxNormal(p, new_min, new_max):
    v = p.copy()
    minA = min(v)
    maxA = max(v)
    dis_A = maxA - minA
    dis_N = new_max - new_min
    for i in range(len(v)):
        v[i] = (v[i] - minA) / dis_A * dis_N + new_min
    return v

def z_scoreNormal(p):
    v = p.copy()
    avg = sum(p) / len(p)
    sigma = math.sqrt(dot(p, p) / len(p) - avg ** 2)
    for i in range(len(v)):
        v[i] = (v[i] - avg) / sigma
    return v


def main():
    print("实验1.习题2.9.9")
    cos_sim_Euc_dis([1, 1, 1, 1], [2, 2, 2, 2])
    cos_sim_Euc_dis([0, 1, 0, 1], [1, 0, 1, 0])
    cos_sim_Euc_dis([2, -1, 0, 2, 0, -3], [-1, 1, -1, 0, 0, -1])
    print("------------------------------------------------")
    print("实验2.习题2.9.10、2.9.11")
    Euc_Man_Che([1, 3, 1, 5, 1], [2, 4, 6, 8, 9])
    Euc_Man_Che_Min([[0, 0], [1, 0], [0, 2]])
    print("------------------------------------------------")
    print("实验3.习题2.9.17")
    p = [2000, 3000, 4000, 6000, 10000]
    print("最小最大规范化:\t", MinMaxNormal(p, 0, 1))
    print("z分数规范化:\t", z_scoreNormal(p))

if __name__ == "__main__":
    main()

