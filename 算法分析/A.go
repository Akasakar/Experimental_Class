/* *
 *    Author:   Akasaka
 *    FileName: A.go
 *    Created:  2019.04.24(UTC+0800) 13.34.04(星期三)
 * */

 package main

 import (
     "fmt"
 )

const _max int = (1 << 10) + 10

var g [_max][_max] int
var idx int

func dfs(r, c, x, y, n int) {
    if n >= 2 {
        var s int = n >> 1
        var tx int = r + s - 1
        var ty int = c + s - 1
        var pos int = (x - r) / s * 2 + (y - c) / s

        idx++

        for i := 0; i < 4; i++ {
            if i != pos {
                g[tx + i / 2][ty + i % 2] = idx
            }
        }

        for i := 0; i < 4; i++ {
            if i == pos {
                dfs(r + i / 2 * s, c + i % 2 * s, x, y, s)
            } else {
                dfs(r + i / 2 * s, c + i % 2 * s, tx + i / 2, ty + i % 2, s)
            }
        }
    }
}

func output(n int) {
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            fmt.Printf("%-4d", g[i][j])
        }
        fmt.Println()
    }
}

 func main() {
     var k, x, y int
     fmt.Scanf("%d%d%d", &k, &x, &y)

     n := 1 << uint(k)

     dfs(0, 0, x - 1, y - 1, n)

     output(n)
 }
