# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: G.py
# Created:  2019.04.29(UTC+0800)10.45.09(星期一)
'''

global n, sum , ans, cnt, g

def printG():
    global n, sum , ans, cnt, g
    print("answer", ans, "#;")
    for i in range(n):
        for j in range(n - i):
            if g[i][j]:
                print("-", end = "")
            else:
                print("+", end = "")
        print("")
    print("-----------------")

def dfs(c):
    global n, sum , ans, cnt, g
    if c == n:
        if cnt[0] == cnt[1]:
            ans += 1
            printG()
    else:
        for x in range(2):
            g[0][c] = bool(x)
            for i in range(1, c + 1):
                g[i][c - i] = g[i - 1][c - i] ^ g[i - 1][c - i + 1]

            for i in range(c + 1):
                cnt[g[i][c - i]] += 1

            if cnt[0] << 1 <= sum and cnt[1] << 1 <= sum:
                dfs(c + 1)

            for i in range(c + 1):
                cnt[g[i][c - i]] -= 1

def main():
    global n, sum , ans, cnt, g
    n = int(input())
    sum = (n + 1) * n // 2
    ans = 0
    cnt = [0, 0]
    g = [[False for j in range(n)] for i in range(n)]

    dfs(0)

    print(ans)

if __name__ == "__main__":
    main()
