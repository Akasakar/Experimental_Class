/* *
 *    Author:   Akasaka
 *    FileName: E.go
 *    Created:  2019.04.28(UTC+0800) 22.48.11(星期日)
 * */

package main

import (
    "fmt"
)

var n, m int
var w, v []int
var dp [][]int

func creatArray(n, m int) ([][]int) {
    var ans [][]int
    for i := 0; i < n; i++ {
        var tmp []int = make([]int, m)
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

func Print(i, j int) {
    if i <= 0 || j <= 0 {
        return
    }
    if dp[i][j] == dp[i - 1][j] {
        Print(i - 1, j)
        fmt.Print("0")
    } else {
        Print(i - 1, j - w[i - 1])
        fmt.Print("1")
    }
}

func main() {
    fmt.Scanf("%d%d", &n, &m)
    dp = creatArray(n + 1, m + 1)
    for i := 0; i < n; i++ {
        var x, y int
        fmt.Scanf("%d%d", &x, &y)
        w = append(w, x)
        v = append(v, y)
    }

    for i := 0; i < n; i++ {
        for j := 0; j <= m; j++ {
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j + w[i] <= m {
                dp[i + 1][j + w[i]] = max(dp[i + 1][j + w[i]], dp[i][j] + v[i])
            }
        }
    }

    fmt.Println(dp[n][m])
    Print(n, m)
}
