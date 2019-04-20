/* *
 *    Author:   Akasaka
 *    FileName: A1.cpp
 *    Created:  2019.04.20(UTC+0800) 12.25.42(星期六)
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

class BigInteger
{
    public:
        //逆序存数字
        vector<int> v;

        BigInteger(){}

        BigInteger(long long s)
        {
            while(s)
            {
                v.push_back(s % 10);
                s /= 10;
            }
        }

        BigInteger(string s)
        {
            for(int i = s.length() - 1; i; i--)
                v.push_back(s[i] - 48);
            if(s[0] == '-') v[v.size() - 1] = -v[v.size() - 1];
            else v.push_back(s[0] - 48);
            ignoreLeadingZero(v);
        }

        string ToString()
        {
            string s="";
            int n = v.size();
            if(v[n - 1] < 0)
            {
                s += '-';
                s += -v[n - 1] + 48;
            }
            else s += v[n -1] + 48;
            for(int i = v.size() - 2; i >= 0; i--)
                s += v[i] + 48;
            return s;
        }

        void push_back(int s)
        {
            v.push_back(s);
        }

        unsigned size()
        {
            return v.size();
        }

        void clear()
        {
            v.clear();
        }

        void add(BigInteger rhs)
        {
            vector<int> &a = v;
            vector<int> &b = rhs.v;
            ignoreLeadingZero(a);
            ignoreLeadingZero(b);
            bool aisNeg = isNegative(a);
            bool bisNeg = isNegative(b);
            if(aisNeg) INV(a);
            if(bisNeg) INV(b);
            if(CompareTo(a, b) < 0)
            {
                swap(a, b);
                swap(aisNeg, bisNeg);
            }
            if(aisNeg)
            {
                if(bisNeg) ADD(a, b);
                else SUB(a, b);
                INV(a);
            }
            else
            {
                if(bisNeg) SUB(a, b);
                else ADD(a, b);
            }
        }

        void sub(BigInteger rhs)
        {
            rhs.ignoreLeadingZero(rhs.v);
            INV(rhs.v);
            add(rhs);
        }

        void mul(BigInteger rhs)
        {
            vector<int> &a = v;
            vector<int> &b = rhs.v;
            bool aisNeg = isNegative(a);
            bool bisNeg = isNegative(b);
            if(aisNeg) INV(a);
            if(bisNeg) INV(b);
            if(CompareTo(a, b) < 0)
            {
                swap(a, b);
                swap(aisNeg, bisNeg);
            }
            MUL(a, b);
            if(aisNeg + bisNeg == 1)
                INV(a);
        }

        void pow10(int k)
        {
            int n = v.size();
            v.resize(v.size() + k);
            for(int i = n - 1; i >= 0; i--)
                v[i + k] = v[i];
            for(int i = 0; i < k; i++)
                v[i] = 0;
        }

        void output()
        {
            vector<int> &a = v;
            puts("output #:");
            for(int i = a.size() - 1; i >= 0; i--)
                printf("%3d", i);
            puts("");
            for(int i = a.size() - 1; i >= 0; i--)
                printf("%3d", a[i]);
            puts("");
        }

    private:

        void ignoreLeadingZero(vector<int> & a)
        {
            for(int i = a.size() - 1; i > 0 && a[i] == 0; i--)
                a.pop_back();
        }

        //保证a,b皆为正数且a>=b
        void ADD(vector<int> &a, vector<int> b)
        {
            b.resize(a.size());
            char c = 0;
            for(int i = 0; i < a.size(); i++)
            {
                a[i] += b[i] + c;
                if(a[i] >= 10)
                {
                    a[i] -= 10;
                    c = 1;
                }
                else c = 0;
            }
            if(c) a.push_back(c);
            ignoreLeadingZero(a);
        }

        //保证a,b皆为正数且a>=b
        void SUB(vector<int> &a, vector<int> b)
        {
            b.resize(a.size());
            char c = 0;
            for(int i = 0; i < a.size(); i++)
            {
                a[i] -= b[i] + c;
                if(a[i] < 0)
                {
                    a[i] += 10;
                    c = 1;
                }
                else c = 0;
            }
            ignoreLeadingZero(a);
        }

        //保证a为正数
        void Carry(vector<int> &a)
        {
            char c = 0;
            for(int i = 0; i < a.size(); i++)
            {
                a[i] += c;
                if(a[i] >= 10)
                {
                    c = a[i] / 10;
                    a[i] %= 10;
                }
                else c = 0;
            }
            if(c) a.push_back(c);
        }

        //保证a,b皆为正数且a>=b
        void MUL(vector<int> &a, vector<int> b)
        {
            vector<int> c;
            for(int i = 0; i < b.size(); i++)
            {
                vector<int> tmp(i);
                for(int j = 0; j < a.size(); j++)
                    tmp.push_back(b[i] * a[j]);
                Carry(tmp);
                ADD(tmp, c);
                c = tmp;
            }
            ignoreLeadingZero(c);
            a = c;
        }

        //保证a,b皆为正数且b<10
        void MULSingle(vector<int> &a, int b)
        {
            for(int i = 0; i < a.size(); i++)
                a[i] = a[i] * b;
            Carry(a);
        }

        //保证a,b皆为正数
        int CompareTo(const vector<int> &a, const vector<int> &b)
        {
            if(a.size() == b.size())
            {
                for(int i = a.size() - 1; i >= 0; i--)
                {
                    if(a[i] == b[i]) continue;
                    return a[i] < b[i] ? -1 : 1;
                }
                return 0;
            }
            return a.size() < b.size() ? -1 : 1;
        }

        //将a取负
        vector<int> INV(vector<int> &a)
        {
            a[a.size() - 1] = -a[a.size() - 1];
            return a;
        }

        //判a负
        bool isNegative(const vector<int> &a)
        {
            return a[a.size() - 1] < 0;
        }
};

void ignoreLeadingZero(vector<int> &a)
{
    for(int i = a.size() - 1; i > 0 && a[i] == 0; i--)
        a.pop_back();
}

//保证a,b皆为正数且a>=b
BigInteger divideMul(BigInteger a, BigInteger b)
{
    if(a.size() == 0 || b.size() == 0) 
        return BigInteger(0);
    if(b.size() == 1)
    {
        a.mul(b);
        return a;
    }
    int na2 = a.size() >> 1;
    int nb2 = b.size() >> 1;
    BigInteger C, D;
    for(int i = 0; i < nb2; i++)
        D.push_back(b.v[i]);
    for(int i = nb2; i < b.size(); i++)
        C.push_back(b.v[i]);
    BigInteger A, B;
    for(int i = 0; i < na2; i++)
        B.push_back(a.v[i]);
    for(int i = nb2; i < na2; i++)
        A.push_back(0);
    for(int i = na2; i < a.size(); i++)
        A.push_back(a.v[i]);
    int n2 = nb2;
    
    //puts("ABCD");
    //A.output();
    //B.output();
    //C.output();
    //D.output();

    BigInteger AC = divideMul(A, C);
    BigInteger BD = divideMul(B, D);
    A.sub(B);
    BigInteger A_B = A;
    D.sub(C);
    BigInteger D_C = D;

    //puts("AC BD A_B D_C");
    //AC.output();
    //BD.output();
    //A_B.output();
    //D_C.output();

    BigInteger A_BD_C = divideMul(A_B, D_C);
    A_BD_C.add(AC);
    A_BD_C.add(BD);

    AC.pow10(n2 << 1);
    A_BD_C.pow10(n2);
    BigInteger ans = AC;
    ans.add(A_BD_C);
    ans.add(BD);
    //puts("ans");
    //ans.output();

    return ans;
}

int main()
{
    string sa, sb;
    while(cin >> sa >> sb)
    {
        //if(sa == "--") break;
        BigInteger a(sa);
        BigInteger b(sb);
        BigInteger c = divideMul(a, b);
        cout << c.ToString() << endl;
    }
    return 0;
}
