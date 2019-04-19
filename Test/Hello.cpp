/* *
 *    Author:   Akasaka
 *    FileName: Hello.cpp
 *    Created:  2019.04.19(UTC+0800) 13.53.48(星期五)
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


#include <bits/stdc++.h>

using namespace std;

int main()
{
    printf("Hello World!");
    return 0;
}
