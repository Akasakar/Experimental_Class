/* *
 *    Author:   Akasaka
 *    FileName: A.cpp
 *    Created:  2019.04.19(UTC+0800) 18.54.16(星期五)
 * */

#define Akasaka

#ifdef Akasaka

#define CPP std::ios::sync_with_stdio(false), std::cin.tie(0), std::cout.tie(0)

#define DebugIN(x)  freopen(x, "r", stdin)
#define DebugOUT(x) freopen(x, "w", stdout)
#define IN  "C:\\Users\\Akasaka\\Desktop\\in.txt"
#define OUT "C:\\Users\\Akasaka\\Desktop\\out.txt"
#define CLOSE   "CON"   ///close in/out.txt
#define STOP system("pause")

#include <ctime>
#define TimeStart   clock_t TIME_START = clock()
#define TimeEnd printf("%ld/%ld",clock() - TIME_START,CLOCKS_PER_SEC)

#else

#pragma comment(linker, "/STACK:102400000,102400000")
#define DebugIN(x)
#define DebugOUT(x)
#define IN
#define OUT
#define STOP

#endif // Akasaka


#include <cstdio>

using namespace std;

const int _max = (1 << 10) + 10;

int g[_max][_max];  //棋盘
int cnt;    //骨牌编号

/* *
 * 棋盘左上角位置 (r, c)，特殊方格位置 (x, y)，棋盘边长 n
 * */
void dfs(int r, int c, int x, int y, int n)
{
    if(n < 2) return;
    int s = n >> 1;
    int tx = r + s - 1;
    int ty = c + s - 1;
    int pos = (x - r) / s * 2 + (y - c) / s;

    cnt++;
    for(int i = 0; i < 4; i++)
    {
        if(i == pos) continue;
        g[tx + i / 2][ty + i % 2] = cnt;
    }

    for(int i = 0; i < 4; i++)
    {
        if(i == pos) dfs(r + i / 2 * s, c + i % 2 * s, x, y, s);
        else dfs(r + i / 2 * s, c + i % 2 * s, tx + i / 2, ty + i % 2, s);
    }
}

int main()
{
    int k, x, y, n; //棋盘大小(2^k*2^k), 特殊方格位置 (x, y)
    scanf("%d%d%d", &k, &x, &y);

    n = 1 << k;
    dfs(0, 0, x - 1, y - 1, n);

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
            printf("%-4d", g[i][j]);
        putchar(10);
    }

    return 0;
}
