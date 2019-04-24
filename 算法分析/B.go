/* *
 *    Author:   Akasaka
 *    FileName: B.go
 *    Created:  2019.04.24(UTC+0800) 14.53.13(星期三)
 * */

package main

import (
    "fmt"
)

const inf int = 0x3f3f3f3f
const _max int = 1000 + 10

var dp [_max][_max] int
var a [_max] int

func min(x, y int) int {
    if x < y {
        return x
    } else {
        return y
    }
}

func solve(i, j int) {
    if i + 1 < j {
        fmt.Printf("(")
    }
    for k := i + 1; k < j; k++ {
        if dp[i][j] == dp[i][k] + dp[k][j] + a[i] * a[k] * a[j] {
            solve(i, k)
            solve(k, j)
            break
        }
    }
    if i + 1 == j {
        fmt.Printf("A%d", i)
    }
    if i + 1 < j {
        fmt.Printf(")")
    }
}

func main() {
    var n int
    fmt.Scanf("%d", &n)
    for i := 1; i <= n; i++ {
        fmt.Scanf("%d%d", &a[i - 1], &a[i])
    }

    for x := 2; x <= n; x++ {
        for i := 0; i + x <= n; i++ {
            j := i + x
            dp[i][j] = inf
            for k := i + 1; k < j; k++ {
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + a[i] * a[k] * a[j])
            }
        }
    }

    fmt.Println(dp[0][n])
    solve(0, n)
}

