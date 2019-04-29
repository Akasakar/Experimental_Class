# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: D.py
# Created:  2019.04.29(UTC+0800)09.23.42(星期一)
'''

global n, v, e, dp

def calc(a, b, c):
    if c == "+":
        return a + b
    else:
        return a * b

def printG(i, j, x):
    global n, v, e, dp
    if i <= j:
        print("(", end = "")
    ti, tj = i % n, j % n
    for k in range(i, j):
        tkl, tkr = k % n, (k + 1) % n
        ok = False
        for p in range(4):
            if dp[ti][tj][x] == calc(dp[ti][tkl][p // 2], dp[tkr][tj][p % 2], e[tkl]):
                printG(i, k, p // 2)
                print(e[tkl], end = "")
                printG(k + 1, j, p % 2)
                ok = True
                break
        if ok:
            break;
    if i == j:
        print(v[ti], end = "")
    if i <= j:
        print(")", end = "")

def main():
    global n, v, e, dp
    n = int(input())
    if n > 0:
        v = list(map(int, input().split()))
    if n > 0:
        e = list(map(str, input().split()))
    dp = [[[0 for k in range(2)] for j in range(n)] for i in range(n)]
    
    for d in range(n):
        for i in range(n):
            if d == 0:
                dp[i][i][0] = dp[i][i][1] = v[i]
            else:
                j, tj = i + d, (i + d) % n
                for k in range(i, j):
                    tkl, tkr = k % n, (k + 1) % n
                    for p in range(4):
                        tmp = calc(dp[i][tkl][p // 2], dp[tkr][tj][p % 2], e[tkl])
                        dp[i][tj][0] = min(dp[i][tj][0], tmp)
                        dp[i][tj][1] = max(dp[i][tj][1], tmp)
    ans = -0x3f3f3f3f
    for i in range(n):
        ans = max(ans, dp[i][(i + n - 1) % n][1])
    print(ans)

    for i in range(n):
        if ans == dp[i][(i + n - 1) % n][1]:
            printG(i, i + n - 1, 1)
            break

if __name__ == "__main__":
    main()
