/* *
 *    Author:   Akasaka
 *    FileName: G.cpp
 *    Created:  2019.04.28(UTC+0800) 12.52.23(星期日)
 * */

#define Akasaka

#ifdef Akasaka

#define CPP std::ios::sync_with_stdio(false), std::cin.tie(0), std::cout.tie(0)

#define DebugIN(x)  freopen(x, "r", stdin)
#define DebugOUT(x) freopen(x, "w", stdout)
#define IN  "./in.in"
#define OUT "./out.out"
#define CLOSE   "CON"   ///close in/out
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


#include <bits/stdc++.h>

using namespace std;

const int _max = 1 << 5;

int n;
int sum;
int ans;
int cnt[2];
bool g[_max][_max];

void printG()
{
    printf("answer %d#:\n", ans);
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j + i < n; j++)
            putchar(g[i][j] ? '-' : '+');
        putchar(10);
    }
    puts("----------------------");
}

void dfs(int c)
{
    if(c == n)
    {
        if(cnt[0] == cnt[1]) 
        {
            ans++;
            printG();   //打印解
        }
        return;
    }
    for(int x = 0; x < 2; x++)
    {
        g[0][c] = x;
        for(int i = 1; i <= c; i++)
            g[i][c - i] = g[i - 1][c - i] ^ g[i - 1][c - i + 1];

        for(int i = 0; i <= c; i++)
            cnt[g[i][c - i]]++;

        if((cnt[0] << 1) <= sum && (cnt[1] << 1) <= sum)
            dfs(c + 1);

        for(int i = 0; i <= c; i++)
            cnt[g[i][c - i]]--;
    }
}

int main()
{
    scanf("%d", &n);
    sum = (n + 1) * n / 2;
    dfs(0);
    printf("%d\n", ans);
    return 0;
}
