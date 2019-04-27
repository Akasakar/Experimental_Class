/* *
 *    Author:   Akasaka
 *    FileName: C.cpp
 *    Created:  2019.04.27(UTC+0800) 10.09.39(星期六)
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
#include <cstdio>
#include <cstring>

using namespace std;

const int _max = 1010;

/* *
 * 长度为 n, m 的两个字符串 s1, s2
 * dp[i][j] 表示 s1[0-i) 和 s2[0-j) 的最长公共子序列
 * 动态转移方程:
 * dp[i + 1][j + 1] = max{dp[i][j + 1], dp[i + 1][j]} (s1[i] != s2[j])
 * dp[i + 1][j + 1] = dp[i][j] + 1 (s1[i] != s2[j])
 * */
int n, m;
char s1[_max], s2[_max];
int dp[_max][_max];

int LCS()
{
    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
        {
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j]);
            if(s1[i] == s2[j])
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1);
        }
    return dp[n][m];
}

void printLCS(int i, int j)
{
    if(i <= 0 || j <= 0) return;
    if(s1[i - 1] == s2[j - 1])
    {
        printLCS(i - 1, j - 1);
        putchar(s1[i - 1]);
    }
    else if(dp[i - 1][j] > dp[i][j - 1])
        printLCS(i - 1, j);
    else 
        printLCS(i, j - 1);
}

int main()
{
    fgets(s1, _max, stdin);
    fgets(s2, _max, stdin);

    n = strlen(s1) - 1;
    m = strlen(s2) - 1;

    printf("%d\n", LCS());

    printLCS(n, m);
    return 0;
}
