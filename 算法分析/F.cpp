/* *
 *    Author:   Akasaka
 *    FileName: F.cpp
 *    Created:  2019.04.28(UTC+0800) 08.15.51(星期日)
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

int n;
int cnt;
vector<vector<int> > vis;
vector<int> c;

void printG()
{
    printf("answer %d#:\n", ++cnt);
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
            if(j == c[i]) putchar(49);
            else putchar(48);
        putchar(10);
    }
    puts("----------------------");
}

void search(int cur)
{
    if(cur == n) printG();
    else for(int j = 0; j < n; j++)
        if(!vis[0][j] && !vis[1][j + cur] && !vis[2][j - cur + n])
        {
            c[cur] = j;
            vis[0][j] = vis[1][j + cur] = vis[2][j - cur + n] = 1;
            search(cur + 1);
            vis[0][j] = vis[1][j + cur] = vis[2][j - cur + n] = 0;
        }
}

int main()
{
    scanf("%d", &n);

    vis = vector<vector<int> >(3, vector<int>(n << 1));
    c = vector<int>(n);

    search(0);

    return 0;
}
