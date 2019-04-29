/* *
 *    Author:   Akasaka
 *    FileName: H.go
 *    Created:  2019.04.29(UTC+0800) 08.48.27(星期一)
 * */

package main

import (
    "fmt"
)

var n, cur, cost int
var vis []bool
var d [][]int
var path, ans []int

func dfs(c int) {
    var u int = path[c - 1]
    if c == n {
        if cur + d[u][0] < cost {
            cost = cur + d[u][0]
            copy(ans, path)
        }
    } else {
        for v := 1; v < n; v++ {
            if !vis[v] && cur + d[u][v] < cost {
                vis[v] = true
                cur += d[u][v]
                path = append(path, v)

                dfs(c + 1)

                path = append(path[:len(path) - 1])
                cur -= d[u][v]
                vis[v] = false
            }
        }
    }
}

func main() {
    fmt.Scanf("%d", &n)

    d, vis, ans = make([][]int, n), make([]bool, n), make([]int, n)
    cost = 0x3f3f3f3f

    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            var x int
            fmt.Scanf("%d", &x)
            d[i] = append(d[i], x)
        }
    }

    path = append(path, 0)
    dfs(1)

    fmt.Println(cost)
    for _, v := range ans {
        fmt.Printf("%d==>", v)
    }
    fmt.Println(0)
}
