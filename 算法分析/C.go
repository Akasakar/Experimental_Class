/* *
 *    Author:   Akasaka
 *    FileName: C.go
 *    Created:  2019.04.27(UTC+0800) 11.32.13(星期六)
 * */

package main

import (
    "fmt"
)

func gets(str *string) {
    var c byte
    var err error
    for {
        _, err = fmt.Scanf("%c", &c)
        if err == nil && c != 10 {
            *str += string(c)
        } else {
            break;
        }
    }
}

func creatArray(n, m int) ([][]int) {
    var ans [][]int
    for i := 0; i < n; i++ {
        var tmp []int = make([]int, m);
        ans = append(ans, tmp)
    }
    return ans
}

func max(a, b int) (int) {
    if a > b {
        return a
    } else {
        return b
    }
}

/* *
 * 长度为 n, m 的两个字符串 s1, s2
 * dp[i][j] 表示 s1[0-i) 和 s2[0-j) 的最长公共子序列
 * 动态转移方程:
 * dp[i + 1][j + 1] = max{dp[i][j + 1], dp[i + 1][j]} (s1[i] != s2[j])
 * dp[i + 1][j + 1] = dp[i][j] + 1 (s1[i] != s2[j])
 * */
var n, m int
var s1, s2 string
var dp[][]int

func LCS() (int) {
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
            if s1[i] == s2[j] {
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)
            }
        }
    }
    return dp[n][m]
}

func printLCS(i, j int) {
    if i > 0 && j > 0 {
        if s1[i - 1] == s2[j - 1] {
            printLCS(i - 1, j - 1);
            fmt.Print(string(s1[i - 1]))
        } else if dp[i - 1][j] > dp[i][j - 1] {
            printLCS(i - 1, j);
        } else {
            printLCS(i, j - 1);
        }
    }
}

func main() {
    gets(&s1)
    gets(&s2)
    n, m = len(s1), len(s2)
    dp = creatArray(n + 1, m + 1)
    fmt.Println(LCS())
    printLCS(n, m)
}
