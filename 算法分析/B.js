
var dp = new Array();
var a = new Array();
var sol = "";

function dfs(i, j)
{
    if(i + 1 < j) sol += "(";
    for(var k = i + 1; k < j; k++)
    {
        if(dp[i][j] == dp[i][k] + dp[k][j] + a[i] * a[k] * a[j])
        {
            dfs(i, k);
            dfs(k, j);
            break;
        }
    }
    if(i + 1 == j) sol += "A" + i;
    if(i + 1 < j) sol += ")";
}

function solve()
{
    var inOBJn = document.getElementById("idn");
    var outOBJ = document.getElementById("matrix");

    var n = parseInt(inOBJn.value);
    a[0] = parseInt(document.getElementById("idl0").value);
    for(var i = 1; i <= n; i++)
    {
        a[i] = parseInt(document.getElementById("idr" + (i - 1)).value);
    }
    for(var i = 0; i <= n; i++)
    {
        dp[i] = new Array();
        for(var j = 0; j <= n; j++)
        {
            dp[i][j] = 0;
        }
    }
    for(var x = 2; x <= n; x++)
    {
        for(var i = 0; i + x <= n; i++)
        {
            var j = i + x;
            dp[i][j] = 0x3f3f3f3f;
            for(var k = i + 1; k < j; k++)
            {
                dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k][j] + a[i] * a[k] * a[j]);
            }
        }
    }
    
    var ans = "<p>" + dp[0][n] + "</p>";
    console.log(ans);
    dfs(0, n);
    ans += "<p>" + sol + "</p>";
    outOBJ.innerHTML = ans;
}

function creatMat(n)
{
    var s = "";
    for(var i = 0; i < n; i++)
    {
        s += "<p>" 
            + "<input id = \"idl" + i 
            + "\" type = \"number\" min = \"1\" max = \"99999999\" required></input>"
            + "<input id = \"idr" + i 
            + "\" type = \"number\" min = \"1\" max = \"99999999\" required></input>"
            + "</p>";
    }
    s += "<button onclick=\"solve()\">Enter</button>";
    return s;
}

function main()
{
    var inOBJn = document.getElementById("idn");
    var outOBJ = document.getElementById("matrix");

    var n = parseInt(inOBJn.value);
    outOBJ.innerHTML = creatMat(n);
}