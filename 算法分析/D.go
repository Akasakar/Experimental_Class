/* *
 *    Author:   Akasaka
 *    FileName: D.go
 *    Created:  2019.04.28(UTC+0800) 22.11.09(星期日)
 * */

package main

import (
    "fmt"
)

const _max int = 1010

/* *
 * dp[i][j] 表示顺/逆时针 v[i]-v[j] 的最优解
 * */
var n int
var v [_max]int
var e [_max]string
var dp [_max][_max][2]int

func min(a, b int) (int) {
    if a < b {
        return a
    } else {
        return b
    }
}

func max(a, b int) (int) {
    if a > b {
        return a
    } else {
        return b
    }
}

func calc(a, b int, c string) (int) {
    if c == "+" {
        return a + b
    } else {
        return a * b
    }
}

func print(i, j, x int) {
    if i == j {
        fmt.Print(v[i % n])
    }
    ti, tj := i % n, j % n
    for k := i; k < j; k++ {
        tkl, tkr := k % n, (k + 1) % n
        var ok bool = false
        for p := 0; p < 4; p++ {
            if dp[ti][tj][x] == calc(dp[ti][tkl][p / 2], dp[tkr][tj][p % 2], e[tkl]) {
                fmt.Print("(")
                print(i, k, p / 2)
                fmt.Print(")", e[tkl], "(")
                print(k + 1, j, p % 2)
                fmt.Print(")")
                ok = true
                break
            }
        }
        if ok {
            break
        }
    }
}

func main() {
    fmt.Scanf("%d", &n)
    for i := 0; i < n; i++ {
        fmt.Scanf("%d", &v[i])
    }
    for i := 0; i < n; i++ {
        fmt.Scanf("%s", &e[i])
    }

    for d := 0; d < n; d++ {
        for i := 0; i < n; i++ {
            if d == 0 {
                dp[i][i][0], dp[i][i][1] = v[i], v[i]
                continue
            }
            var j, tj int = i + d, (i + d) % n
            for k := i; k < j; k++ {
                var tkl, tkr int = k % n, (k + 1) % n
                var tmp int
                for p := 0; p < 4; p++ {
                    tmp = calc(dp[i][tkl][p / 2], dp[tkr][tj][p % 2], e[tkl])
                    dp[i][tj][0] = min(dp[i][tj][0], tmp)
                    dp[i][tj][1] = max(dp[i][tj][1], tmp)
                }
            }
        }
    }

    var ans int = -0x3f3f3f3f
    for i := 0; i < n; i++ {
        ans = max(ans, dp[i][(i + n - 1) % n][1])
    }
    fmt.Println(ans)
    for i := 0; i < n; i++ {
        if ans == dp[i][(i + n - 1) % n][1] {
            print(i, i + n - 1, 1)
            break
        }
    }
}
