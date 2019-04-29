/* *
 *    Author:   Akasaka
 *    FileName: H.cpp
 *    Created:  2019.04.28(UTC+0800) 19.06.01(星期日)
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


#include <vector>
#include <cstdio>

using namespace std;

const int inf = 0x3f3f3f3f;

/* *
 * 测试数据
输入:
4
0 30 8 7
30 0 4 5
8 4 0 10
7 5 10 0
输出:
24
0==>2==>1==>3==>0
 * */

int n;
vector<vector<int> > d;
vector<int> path, ans;
vector<bool> vis;
int cur, cost = inf;

/* *
 * 暴搜+
void dfs(int c)
{
    int u = 0;
    if(c != 0) u = path[c -1];

    if(c == n)
    {
        if(cur + d[u][0] < cost)
        {
            cost = cur + d[u][0];
            ans = path;
        }
        return;
    }
    for(int v = 0; v < n; v++)
        if(!vis[v] && cur  + d[u][v] + d[v][0] < cost)
        {
            vis[v] = 1;
            path.push_back(v);
            cur += d[u][v];

            dfs(c + 1);

            cur -= d[u][v];
            path.pop_back();
            vis[v] = 0;
        }
}

int main()
{
    scanf("%d", &n);

    vis = vector<bool>(n);
    d = vector<vector<int> >(n);

    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
        {
            int x;
            scanf("%d", &x);
            d[i].push_back(x);
        }

    dfs(0);

    printf("%d\n", cost);
    for(int i = 0; i < ans.size(); i++)
        printf("%d==>", ans[i]);
    puts("0");

    return 0;
}
