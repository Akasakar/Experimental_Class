# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: A.py
# Created:  2019.04.20(UTC+0800)20.21.47(星期六)
'''

global g, idx

def dfs(r, c, x, y, n):
    if n < 2:
        return
    s = n >> 1;
    tx = r + s - 1
    ty = c + s - 1
    pos = (x - r) // s * 2 + (y - c) // s

    global g, idx
    idx += 1
    for i in range(4):
        if i == pos:
            continue
        g[tx + i // 2][ty + i % 2] = idx;

    for i in range(4):
        if i == pos:
            dfs(r + i // 2 * s, c + i % 2 * s, x, y, s)
        else:
            dfs(r + i // 2 * s, c + i % 2 * s, tx + i // 2, ty + i % 2, s)

def main():
    k, x, y = map(int, input().split());

    global g, idx
    idx = 0
    n = 1 << k
    g = [[0 for i in range(n)] for j in range(n)]

    dfs(0, 0, x - 1, y - 1, n)

    for i in range(n):
        print(g[i])

if __name__ == '__main__':
    main()
