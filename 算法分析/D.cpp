/* *
 *    Author:   Akasaka
 *    FileName: D.cpp
 *    Created:  2019.04.27(UTC+0800) 19.22.44(星期六)
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

const int _max = 1010;

/* *
 * dp[i][j] 表示顺/逆时针 v[i]-v[j] 的最优解
 * */
int n;
int v[_max], e[_max];
int dp[_max][_max][2];

int calc(int a, int b, char c)
{
    if(c == '+') return a + b;
    else return a * b;
}

void print(int i, int j, int x)
{
    if(i <= j) putchar('(');
    int ti = i % n;
    int tj = j % n;
    for(int k = i; k < j; k++)
    {
        int tkl = k % n;
        int tkr = (k + 1) % n;
        bool ok = 0;
        for(int p = 0; p < 4; p++)
            if(dp[ti][tj][x] == calc(dp[ti][tkl][p / 2], dp[tkr][tj][p % 2], e[tkl]))
            {
                print(i, k, p / 2);
                putchar(e[tkl]);
                print(k + 1, j, p % 2);
                ok = 1;
                break;
            }
        if(ok) break;
    }
    if(i == j) printf("%d", v[ti]);
    if(i <= j) putchar(')');
}

int main()
{
    scanf("%d", &n);
    for(int i = 0; i < n; i++)
        scanf("%d", v + i);
    getchar();
    for(int i = 0; i < n; i++)
    {
        e[i] = getchar();
        getchar();
    }

    for(int d = 0; d < n; d++)
        for(int i = 0; i < n; i++)
        {
            if(d == 0)
            {
                dp[i][i][0] = dp[i][i][1] = v[i];
                continue;
            }
            int j = i + d;
            int tj = j % n;
            for(int k = i; k < j; k++)
            {
                int tkl = k % n;
                int tkr = (k + 1) % n;
                for(int p = 0; p < 4; p++)
                {
                    dp[i][tj][0] = min(dp[i][tj][0], calc(dp[i][tkl][p / 2], dp[tkr][tj][p % 2], e[tkl]));
                    dp[i][tj][1] = max(dp[i][tj][1], calc(dp[i][tkl][p / 2], dp[tkr][tj][p % 2], e[tkl]));
                }
            }
        }

    int ans = -0x3f3f3f3f;
    for(int i = 0; i < n; i++)
        ans = max(ans, dp[i][(i + n - 1) % n][1]);
    printf("%d\n", ans);
    for(int i = 0; i < n; i++)
        if(ans == dp[i][(i + n - 1) % n][1])
        {
            print(i, i + n - 1, 1);
            break;
        }
    return 0;
}
