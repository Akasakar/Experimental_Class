/* *
 *    Author:   Akasaka
 *    FileName: G.go
 *    Created:  2019.04.29(UTC+0800) 08.15.51(星期一)
 * */

package main

import (
    "fmt"
)

var n, sum, ans int
var cnt [2]int
var g [][]int

func creatArray(n, m int) ([][]int) {
    var ans [][]int
    for i := 0; i < n; i++ {
        //var tmp []int = make([]int, m)
        ans = append(ans, make([]int, m))
    }
    return ans
}

func printG() {
    fmt.Printf("anwser %d#:\n", ans)
    for i := 0; i < n; i++ {
        for j := 0; j + i < n; j++ {
            if g[i][j] > 0 {
                fmt.Print("-")
            } else {
                fmt.Print("+")
            }
        }
        fmt.Println("")
    }
    fmt.Println("-----------------")
}

func dfs(c int) {
    if c == n {
        if cnt[0] == cnt[1] {
            ans++
            printG()
        }
    } else {
        for x := 0; x < 2; x++ {
            g[0][c] = x
            for i := 1; i <= c; i++ {
                g[i][c - i] = g[i - 1][c - i] ^ g[i - 1][c - i + 1]
            }
            for i := 0; i <= c; i++ {
                cnt[g[i][c - i]]++
            }

            if cnt[0] << 1 <= sum && cnt[1] << 1 <= sum {
                dfs(c + 1)
            }

            for i := 0; i <= c; i++ {
                cnt[g[i][c - i]]--
            }
        }
    }
}

func main() {
    fmt.Scanf("%d", &n)
    g = creatArray(n, n)
    sum = (n + 1) * n / 2
    dfs(0)
    fmt.Println(ans)
}
