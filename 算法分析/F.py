# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: F.py
# Created:  2019.04.29(UTC+0800)10.31.01(星期一)
'''

global n, cnt, c, vis

def printG():
    print("answer", cnt, "#:")
    for i in range(n):
        for j in range(n):
            if j == c[i]:
                print("1", end = "")
            else:
                print("0", end = "")
        print("")
    print("-----------------")

def search(cur):
    global n, cnt, c, vis
    if cur == n:
        cnt += 1
        printG()
    else:
        for j in range(n):
            if not(vis[0][j] or vis[1][j + cur] or vis[2][j - cur + n]):
                c[cur] = j
                vis[0][j] = vis[1][j + cur] = vis[2][j - cur + n] = True
                search(cur + 1)
                vis[0][j] = vis[1][j + cur] = vis[2][j - cur + n] = False

def main():
    global n, cnt, c, vis
    n = int(input())
    cnt = 0
    vis = [[False for j in range(n << 1)] for i in range(3)]
    c = [0 for i in range(n)]

    search(0)
    
if __name__ == "__main__":
    main()
