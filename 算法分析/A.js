
var g = new Array();
var idx = 0;

function dfs(r, c, x, y, n)
{
    if(n < 2) return;
    var s = n >> 1;
    var tx = r + s - 1;
    var ty = c + s - 1;
    var pos = (x - r) / s * 2 + (y - c) / s;

    idx++;
    for(var i = 0; i < 4; i++)
    {
        if(i == pos) continue;
        g[tx + Math.floor(i / 2)][ty + i % 2] = idx;
    }

    for(var i = 0; i < 4; i++)
    {
        if(i == pos) dfs(r + i / 2 * s, c + i % 2 * s, x, y, s);
        else dfs(r + Math.floor(i / 2) * s, c + i % 2 * s, tx + Math.floor(i / 2), ty + i % 2, s);
    }
}

function output(n)
{
    var s = "";
    for(var i = 0; i < n; i++)
    {
        s += "<p>[" + g[i][0];
        for(var j = 1; j < n; j++)
        {
            s += ", " + g[i][j];
        }
        s += "]</p>";
    }
    return s;
}

function main() 
{
    var inOBJk = document.getElementById("idk");
    var inOBJx = document.getElementById("idx");
    var inOBJy = document.getElementById("idy");

    var outOBJ = document.getElementById("output");
    var debug = document.getElementById("debug");

    var k = parseInt(inOBJk.value);
    var x = parseInt(inOBJx.value);
    var y = parseInt(inOBJy.value);

    var n = (1 << k);

    for (var i = 0; i < n; i++)
    {
        g[i] = new Array();
    }
    for (var i = 0; i < n; i++)
    {
        for(var j = 0; j < n; j++)
        {
            g[i][j] = 0;
        }
    }

    dfs(0, 0, x - 1, y - 1, n);

    outOBJ.innerHTML = output(n);
}