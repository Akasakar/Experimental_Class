# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: E.py
# Created:  2019.04.29(UTC+0800)10.03.01(星期一)
'''

global n, m, w, v, dp

def printA(i, j):
    if i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j]:
            printA(i - 1, j)
            print("0", end = "")
        else:
            printA(i - 1, j - w[i - 1])
            print("1", end = "")

def main():
    global n, m, w, v, dp
    n, m = map(int, input().split())

    w = []
    v = []
    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

    for i in range(n):
        x, y = map(int, input().split())
        w.append(x)
        v.append(y)

    for i in range(n):
        for j in range(m + 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j + w[i] <= m:
                dp[i + 1][j + w[i]] = max(dp[i + 1][j + w[i]], dp[i][j] + v[i])

    print(dp[n][m])

    printA(n, m)

if __name__ == "__main__":
    main()
