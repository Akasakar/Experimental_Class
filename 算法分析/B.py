# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: B.py
# Created:  2019.04.22(UTC+0800)09.40.26(星期一)
'''

global dp, a

def solve(i, j):
    if i + 1 < j:
        print('(', end='')
    
    global dp, a

    for k in range(i + 1, j):
        if dp[i][j] == dp[i][k] + dp[k][j] + a[i] * a[k] * a[j]:
            solve(i, k)
            solve(k, j)
            break;

    if i + 1 == j:
        print("A%d" % i, end='')
    if i + 1 < j:
        print(')', end='')

def main():
    n = int(input())

    global dp, a
    a = list(map(int, input().split()))
    dp = [[0 for j in range(n + 10)] for i in range(n + 10)]

    for x in range(2, n + 1):
        for i in range(n - x + 1):
            j = i + x
            dp[i][j] = int(0x3f3f3f3f)
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + a[i] * a[k] * a[j])

    print(dp[0][n])
    solve(0, n)

if __name__ == '__main__':
    print(__name__)
    main()
