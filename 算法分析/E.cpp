/* *
 *    Author:   Akasaka
 *    FileName: E.cpp
 *    Created:  2019.04.27(UTC+0800) 23.04.09(星期六)
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


#include <algorithm>
#include <vector>
#include <cstdio>

using namespace std;

/* *
 * n 个物品，背包负重 m
 * 接下来给出 n 个物品的信息
 * 第i个物品重量w[i]，价值v[i]
 * dp[i][j] 表示前i个物品装下重j之后的价值
 * 转移方程:
 * dp[i + 1][j] = max(dp[i + 1][j], dp[i][j]);
 * dp[i + 1][j + w[i]] = max(dp[i + 1][j + w[i]], dp[i][j] + v[i]);
 * */
int n, m;
vector<int> w, v;
vector<vector<int> > dp;

void print(int i, int j)
{
    if(i <= 0 || j <= 0) return;
    if(dp[i][j] == dp[i - 1][j])
    {
        print(i - 1, j);
        printf("0");
    }
    else
    {
        print(i - 1, j - w[i - 1]);
        printf("1");
    }
}

int main()
{
    scanf("%d%d", &n, &m);
    dp = vector<vector<int> >(n + 1, vector<int>(m + 1));
    for(int i = 0; i < n; i++)
    {
        int x, y;
        scanf("%d%d", &x, &y);
        w.push_back(x);
        v.push_back(y);
    }

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j <= m; j++)
        {
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j]);
            if(j + w[i] <= m)
                dp[i + 1][j + w[i]] = max(dp[i + 1][j + w[i]], dp[i][j] + v[i]);
        }
    }

    printf("%d\n", dp[n][m]);
    print(n, m);

    return 0;
}
