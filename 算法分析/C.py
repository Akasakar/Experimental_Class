# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: C.py
# Created:  2019.04.27(UTC+0800)14.34.09(星期六)
'''
import sys

'''
# 长度为 n, m 的两个字符串 s1, s2
# dp[i][j] 表示 s1[0-i) 和 s2[0-j) 的最长公共子序列
# 动态转移方程:
# dp[i + 1][j + 1] = max{dp[i][j + 1], dp[i + 1][j]} (s1[i] != s2[j])
# dp[i + 1][j + 1] = dp[i][j] + 1 (s1[i] != s2[j])
'''
global n, m, s1, s2, dp

def LCS():
    global n, m, s1, s2, dp
    for i in range(n):
        for j in range(m):
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
    return dp[n][m]

def printLCS(i, j):
    if i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            printLCS(i - 1, j - 1)
            print(s1[i - 1], end = "")
        elif dp[i - 1][j] > dp[i][j - 1]:
            printLCS(i - 1, j)
        else:
            printLCS(i, j - 1)

def main():
    global n, m, s1, s2, dp
    s1, s2 = input(), input()
    n, m = len(s1), len(s2)
    dp = [[0 for j in range(m + 1)]for i in range(n + 1)]
    print(LCS())
    printLCS(n, m)

if __name__ == "__main__":
    main()
