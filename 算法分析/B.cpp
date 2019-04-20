/* *
 *    Author:   Akasaka
 *    FileName: B.cpp
 *    Created:  2019.04.20(UTC+0800) 18.46.44(星期六)
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


#include <algorithm>
#include <cstdio>

using namespace std;

const int inf = 0x3f3f3f3f;
const int _max = 1000 + 10;

int dp[_max][_max];
int a[_max];

//矩阵括号位置
void solve(int i, int j)
{
    if(i + 1 < j) putchar('(');
    for(int k = i + 1; k < j; k++)
        if(dp[i][j] == dp[i][k] + dp[k][j] + a[i] * a[k] * a[j])
        {
            solve(i, k);
            solve(k, j);
            break;
        }
    if(i + 1 == j) printf("A%d", i);
    if(i + 1 < j) putchar(')');
}

int main()
{
    int n;  //矩阵数
    scanf("%d", &n);
    for(int i = 1; i <= n; i++) //输入矩阵行列数
        scanf("%d%d", a + i - 1, a + i);

    for(int x = 2; x <= n; x++)
        for(int i = 0; i + x <= n; i++)
        {
            int j = i + x;
            dp[i][j] = inf;
            for(int k = i + 1; k < j; k++)
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + a[i] * a[k] * a[j]);
        }

    printf("%d\n", dp[0][n]);
    solve(0, n);
    return 0;
}
