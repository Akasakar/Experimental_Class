# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: F.py
# Created:  2019.05.25(UTC+0800)10.35.36(星期六)
'''


import pandas
import random
import math

def sign(x):
    if x > 0:
        return 1
    else:
        return -1

def perceptron(train):
    # 初始化权值， w[i][-1] 表示阈值(Theta)
    w = [[0.0 for j in range(len(train[0]))] for i in range(2)]
    w[1][-1] = random.random()
    # 精度，学习率
    eps, eta = 1e-6, 0.9
    # 训练 1000 轮
    for t in range(1000):
        # 学习率下降
        eta = eta / 233 * 199
        w[0], sw = w[1].copy(), [0.0 for i in range(len(w[0]))]
        # 开始学习
        for dr in train:
            tmp = eta * (sign(dr[-1]) - sign(sum([w[0][i] * dr[i] for i in range(len(dr) - 1)]) > w[0][-1]))
            X = [dr[i] * tmp for i in range(len(dr) - 1)] + [-tmp]
            Y = [w[0][i] + X[i] for i in range(len(X))]
            sw = [sw[i] + Y[i] for i in range(len(sw))]
        # 得到平均学习权值
        w[1] = [x / len(train) for x in sw]
        # 与上一轮权值比较无变化，跳出
        if sum([abs(w[0][i] - w[1][i]) < eps for i in range(len(w[0]))]) >= len(w[0]):
            break
    return w[0]

def main():
    data = pandas.read_csv("实验6-iris-人工神经网络.txt", header = None).values.tolist()
    data = list(map(lambda dr: [dr[0], dr[1], int(dr[-1])], data))
    random.shuffle(data)
    # 前9份训练，最后1份测试
    train, test = data[:len(data) // 10 * 9], data[len(data) // 10 * 9:]
    w = perceptron(train)
    print(w)
    '''
    print("Train")
    for t in train:
        s = "Expect({0}) ForeCast({1}) ==> {2}"
        FC = int(sum([w[i] * t[i] for i in range(len(w) - 1)]) > w[-1])
        print(t[:-1], s.format(t[-1], FC, ["Wa", "Ac"][t[-1] == FC]))
    '''
    print("Test")
    for t in test:
        s = "Expect({0}) ForeCast({1}) ==> {2}"
        FC = int(sum([w[i] * t[i] for i in range(len(w) - 1)]) > w[-1])
        print(t[:-1], s.format(t[-1], FC, ["Wa", "Ac"][t[-1] == FC]))

if __name__ == "__main__":
    main()
