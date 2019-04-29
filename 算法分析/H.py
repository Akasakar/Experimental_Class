# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: H.py
# Created:  2019.04.29(UTC+0800)10.57.46(星期一)
'''

global n, d, path, ans, vis, cur, cost

def dfs(c):
    global n, d, path, ans, vis, cur, cost
    u = path[c - 1]
    if c == n:
        if cur + d[u][0] < cost:
            cost = cur + d[u][0]
            ans = path.copy()
    else:
        for v in range(1, n):
            if not(vis[v] or cur + d[u][v] >= cost):
                vis[v] = True
                cur += d[u][v]
                path.append(v)

                dfs(c + 1)

                path.pop()
                cur -= d[u][v]
                vis[v] = False

def main():
    global n, d, path, ans, vis, cur, cost
    n = int(input())
    d = [[] for i in range(n)]
    path, ans = [0], []
    vis = [False for i in range(n)]
    cur, cost = 0, 0x3f3f3f3f

    for i in range(n):
        d[i] = list(map(int, input().split()))

    dfs(1)
    
    print(cost)
    for v in ans:
        print(v, "==>", end = " ")
    print("0")

if __name__ == "__main__":
    main()
