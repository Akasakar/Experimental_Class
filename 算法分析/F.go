/* *
 *    Author:   Akasaka
 *    FileName: F.go
 *    Created:  2019.04.29(UTC+0800) 07.56.27(星期一)
 * */

package main

import (
    "fmt"
)

var n, cnt int
var c []int
var vis [][]bool

func crearArray(n, m int) ([][]bool) {
    var ans [][]bool
    for i := 0; i < n; i++ {
        var tmp []bool = make([]bool, m)
        ans = append(ans, tmp)
    }
    return ans
}

func printG() {
    fmt.Printf("answer %d#:\n", cnt)
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            if j == c[i] {
                fmt.Print(1)
            } else {
                fmt.Print(0)
            }
        }
        fmt.Println("")
    }
    fmt.Println("-------------------")
}

func search(cur int) {
    if cur == n {
        cnt++
        printG()
    } else {
        for j := 0; j < n; j++ {
            if !vis[0][j] && !vis[1][j + cur] && !vis[2][j - cur + n] {
                c[cur] = j
                vis[0][j], vis[1][j + cur], vis[2][j - cur + n] = true, true, true
                search(cur + 1)
                vis[0][j], vis[1][j + cur], vis[2][j - cur + n] = false, false, false
            }
        }
    }
}

func main() {
    fmt.Scanf("%d", &n)
    c = make([]int, n)
    vis = crearArray(3, n << 1)

    search(0)
}
