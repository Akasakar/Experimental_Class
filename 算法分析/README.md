# 也不知道写什么，随便写一点好了  
>## 实验一：棋盘覆盖问题
>其实应该叫三格骨牌问题(《算法谜题》看到过)  
>>### 内容:  
>>输入特殊方格的位置以及棋盘大小（2k个方格即输入k），用分治法实现L型骨牌覆盖磁盘问题，计算结果显示棋盘骨牌覆盖情况（用数字表示）  
>
>>### 题解:  
>>最直白的分治即可  
>>> ![棋盘覆盖](https://gss3.bdstatic.com/7Po3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike80%2C5%2C5%2C80%2C26/sign=fe265636ce177f3e0439f45f11a650a2/0bd162d9f2d3572c3e31585c8d13632763d0c35b.jpg)  
>>>填上黄色骨牌后，将棋盘二分为四个相等的子棋盘，子棋盘和原问题一致，即子问题，简单分治即可  
>>>  
>>>棋盘左上角位置 (r, c)，特殊方格位置 (x, y)，棋盘边长 n
>>>每次对填骨牌，其实都知道了骨牌位置，所以直接记下位置作为参数即可，每次划分出的子棋盘只需要算出相对位置即可，故记录棋盘左上角位置作为参数，记录一下棋盘边长n  
>>>```cpp
>>>//(tx,ty)表示棋盘中间位置，且为左上角块
>>>void dfs(int r, int c, int x, int y, int n)
>>>{
>>>    if(n < 2) return;
>>>    int s = n >> 1;
>>>    int tx = r + s - 1;
>>>    int ty = c + s - 1;
>>>    int pos = (x - r) / s * 2 + (y - c) / s;
>>>
>>>    cnt++;
>>>    for(int i = 0; i < 4; i++)
>>>    {
>>>        if(i == pos) continue;
>>>        g[tx + i / 2][ty + i % 2] = cnt;
>>>    }
>>>
>>>    for(int i = 0; i < 4; i++)
>>>    {
>>>        if(i == pos) dfs(r + i / 2 * s, c + i % 2 * s, x, y, s);
>>>        else dfs(r + i / 2 * s, c + i % 2 * s, tx + i / 2, ty + i % 2, s);
>>>    }
>>>}
>>>```  
>
>## 实验二：矩阵连乘问题  
>>### 内容:  
>>n个矩阵连乘，不满足交换律，但是满足结合律，通过不同的加括号方式，会使得需要的乘法次数不同。用动态规划方法计算，找出最优加括号方式，使总的乘法次数最少。  
>
>>### 题解:  
>>简单dp，dp[i][j]表示区间 [i, j) 矩阵乘法最优值，a[i]表示第i个矩阵的行数，其中a[n]表示第n-1个矩阵的列数，动态转移方程如下  
>>>```cpp
>>>dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + a[i] * a[k] * a[j]);
>>>```  
>>>给出一种打印连乘的方式
>>>```cpp
>>>void solve(int i, int j)
>>>{
>>>    if(i + 1 < j) putchar('(');
>>>    for(int k = i + 1; k < j; k++)
>>>        if(dp[i][j] == dp[i][k] + dp[k][j] + a[i] * a[k] * a[j])
>>>        {
>>>            solve(i, k);
>>>             //这里可以输出乘法符号
>>>            solve(k, j);
>>>            break;
>>>        }
>>>    if(i + 1 == j) printf("A%d", i);
>>>    if(i + 1 < j) putchar(')');
>>>}
>>>```  
>
>## 实验三：最长公共子序列问题  
>>### 内容:  
>>输入两个相同类型的序列，用动态规划方法计算他们的最长公共子序列的长度以及序列。  
>
>>### 题解:  
>>简单dp，dp[i][j]表示s1[0-i), s2[0-j) 的最长公共字串，动态转移方程如下  
>>>```cpp
>>>if(s1[i] != s2[j])
>>>    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j]);
>>>if(s1[i] == s2[j])
>>>    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1);
>>>```  
>>>给出一种打印最长字串的方式
>>>```cpp
>>>void printLCS(int i, int j)
>>>{
>>>    if(i <= 0 || j <= 0) return;
>>>    if(s1[i - 1] == s2[j - 1])
>>>    {
>>>        printLCS(i - 1, j - 1);
>>>        putchar(s1[i - 1]);
>>>    }
>>>    else if(dp[i - 1][j] > dp[i][j - 1])
>>>        printLCS(i - 1, j);
>>>    else 
>>>        printLCS(i, j - 1);
>>>}
>>>```  
>
>## 实验四：多边形游戏问题  
>>### 内容:  
>>按照要求输入多边形的边和顶点，游戏第一步： 删除一条边， 随后的n-1步按以下方式操作：
>>   1）选择一条边E以及由E连接着的2个顶点v1和v2
>>   2）用一个新的顶点取代边E以及由E连着的2个顶点v1和v2。将由顶点v1和v2的整数值通过边E上的运算得到的结果赋予新顶点。直到最后，所有边被删除，确认使结果达到最大值的删除方式和最大值。  
>
>>### 题解:  
>>![多边形游戏](https://img-my.csdn.net/uploads/201203/22/0_1332411346tu0M.gif)简单dp，dp[i][j][x] 表示顺/逆时针 v[i]-v[j] 的最优解(x为0时表示最小值，1为最大值)，v[i]表示顶点i权值,e[i]表示起始端点为v[i]的边，和矩阵连乘一样，故不再赘述，详细看[D.cpp](D.cpp)  
>>>给出一种打印解的方式
>>>```cpp
>>>void print(int i, int j, int x)
>>>{
>>>    if(i <= j) putchar('(');
>>>    int ti = i % n;
>>>    int tj = j % n;
>>>    for(int k = i; k < j; k++)
>>>    {
>>>        int tkl = k % n;
>>>        int tkr = (k + 1) % n;
>>>        bool ok = 0;
>>>        for(int p = 0; p < 4; p++)
>>>            if(dp[ti][tj][x] == calc(dp[ti][tkl][p / 2], dp[tkr][tj][p % 2], e[tkl]))
>>>            {
>>>                print(i, k, p / 2);
>>>                putchar(e[tkl]);
>>>                print(k + 1, j, p % 2);
>>>                ok = 1;
>>>                break;
>>>            }
>>>        if(ok) break;
>>>    }
>>>    if(i == j) printf("%d", v[ti]);
>>>    if(i <= j) putchar(')');
>>>}
>>>```  
>
>## 实验五：0-1背包问题  
>>### 内容:  
>>给定n种物品和一个背包，物品i价值wi和重量vi已知，确定装入背包的物品方案，使得包内物品总价值最大。
>>我们改一下，变成weight表示重量，value表示价值    
>
>>### 题解:  
>>针对每个物品是否放入背包进行暴搜试试  
>>>```cpp
>>>//输入
>>>int n, W;
>>>int w[MAX_N], v[MAX_N];
>>>//从第i个物品开始挑选总重小于j的部分
>>>int rec(int i, int j)
>>>{
>>>    int res;
>>>    if(i == n) res = 0; //已经，没有剩余物品了
>>>    else if(j < w[i]) res = rec(i + 1, j);  //无法挑选这个物品
>>>    else res = max(rec(i + 1, j), rec(i + 1, j - w[i]) + v[i]); //挑选和不挑选两种情况都尝试一下
>>>    return res;
>>>}
>>>```  
>>
>> 这里其实可以记录一下每一步的状态，用一个数组dp[i][j]记录状态rec(i,j)复杂度可以从 O(2^n) 降至 O(n^2),现在就叫做记忆化搜索了  
>>>```cpp
>>>int dp[MAX_N + 1][MAX_W + 1];
>>>int rec(int i, int j)
>>>{
>>>    int &res = dp[i][j];
>>>    if(rec != 0) return rec;
>>>    if(i == n) res = 0; //已经，没有剩余物品了
>>>    else if(j < w[i]) res = rec(i + 1, j);  //无法挑选这个物品
>>>    else res = max(rec(i + 1, j), rec(i + 1, j - w[i]) + v[i]); //挑选和不挑选两种情况都尝试一下
>>>    return res;
>>>}
>>>```  
>> 动态转移方程如下
>>>```go
>>>dp[n][j] = 0
>>>if j < w[i] {
>>>    dp[i][j] = dp[i + 1][j]    
>>>} else {
>>>    dp[i][j] = max(dp[i + 1][j], dp[i + 1][j - w[i]] + v[i])
>>>}
>>>```  
>
>## 实验六：n后问题  
>>### 内容:  
>>确定国际象棋棋盘上的n个皇后的位置，使之不位于同一行，同一列，同一斜线上的最佳方案。    
>
>>### 题解:  
>>就是一个简单搜索，顺便回朔一下就可以了，vis[0][j]表示第j列有没有皇后，vis[1][j + cur]表示主对角线有没有皇后，vis[2][j - cur + n]表示主副角线有没有皇后，c[cur]记录一下第cur行皇后在第j列，枚举第cur行皇后状态即可，注意回朔，c数组可用来打印解，若不需要打印可删减  
>>>```py
>>>#python
>>>def search(cur):
>>>    global n, cnt, c, vis
>>>    if cur == n:
>>>        cnt += 1
>>>        printG()
>>>    else:
>>>        for j in range(n):
>>>            if not(vis[0][j] or vis[1][j + cur] or vis[2][j - cur + n]):
>>>                c[cur] = j
>>>                vis[0][j] = vis[1][j + cur] = vis[2][j - cur + n] = True
>>>                search(cur + 1)
>>>                vis[0][j] = vis[1][j + cur] = vis[2][j - cur + n] = False    #这里清0回朔
>>>```  
>
>## 实验七：符号三角形问题  
>>### 内容:  
>>确定一行n个符号（+号或-号）按照同或的规则，向下生成三角形，确定三角形中+号个数和-号个数相等的符号三角形的个数。  
>
>>### 题解:  
>>暴搜+剪枝，同样没什么好说的，这里可以用二进制模拟，可减小内存开支，STL选择bitset，cnt[x]表示符号'x'个数，sum表示符号总数，显然这个符号三角形一旦第一行确定了，剩下的都确定了，所以只需要枚举第一行的状态即可，即在n位二进制下模拟01，状态数2^n，当然要剪枝，不然炸了，在模拟过程中就可以适当的剪枝，显然cnt[x] * 2 > sum时不满足条件，剪掉这种情况，剩下的cnt[0]=cnt[1]都是符合要求的解  
>>>```cpp
>>>void dfs(int c)
>>>{
>>>    if(c == n)
>>>    {
>>>        if(cnt[0] == cnt[1]) 
>>>        {
>>>            ans++;
>>>            printG();   //打印解
>>>        }
>>>        return;
>>>    }
>>>    for(int x = 0; x < 2; x++)
>>>    {
>>>        g[0][c] = x;
>>>        for(int i = 1; i <= c; i++)
>>>            g[i][c - i] = g[i - 1][c - i] ^ g[i - 1][c - i + 1];
>>>
>>>        for(int i = 0; i <= c; i++)
>>>            cnt[g[i][c - i]]++;
>>>
>>>        if((cnt[0] << 1) <= sum && (cnt[1] << 1) <= sum)
>>>            dfs(c + 1);
>>>
>>>        for(int i = 0; i <= c; i++)
>>>            cnt[g[i][c - i]]--;
>>>    }
>>>}
>>>```  
>
>## 实验八：旅行售货员问题  
>>### 内容:  
>>旅行售货员从一个城市出发，确定他从每个城市经过且只经过一次的情况下，最短路径。  
>
>>### 题解:  
>>暴搜+剪枝,这个问题没有什么特别好的方法，暴力点搜索就好，注意剪枝，如果后面的解不优于前面搜索到的解，就剪掉，玄学搜索，越早搜到最优值，后面的次优值都可剪掉  
>>>```go
>>>//go语言
>>>func dfs(c int) {
>>>    var u int = path[c - 1]
>>>    if c == n {
>>>        if cur + d[u][0] < cost {
>>>            cost = cur + d[u][0]
>>>            copy(ans, path)
>>>        }
>>>    } else {
>>>        for v := 1; v < n; v++ {
>>>            if !vis[v] && cur + d[u][v] < cost {
>>>                vis[v] = true
>>>                cur += d[u][v]
>>>                path = append(path, v)
>>>
>>>                dfs(c + 1)
>>>
>>>                path = append(path[:len(path) - 1])
>>>                cur -= d[u][v]
>>>                vis[v] = false
>>>            }
>>>        }
>>>    }
>>>}
>>>```  

