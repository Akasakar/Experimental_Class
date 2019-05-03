var dp = new Array();
var a = new Array();
var ans = "";

function printG(i, j)
{
    if(i + 1 == j) ans += "A<sub>" + a[i] + "*" + a[i + 1] + "</sub>";
    for(var k = i + 1; k < j; k++)
        if(dp[i][j] == dp[i][k] + dp[k][j] + a[i] * a[k] * a[j])
        {
            ans += "("
            printG(i, k);
            ans += ")*("
            printG(k, j);
            ans += ")";
            break;
        }
}

function solve(n)
{
    for(var x = 2; x <= n; x++)
        for(var i = 0; i + x <= n; i++)
        {
            var j = i + x;
            dp[i][j] = 9999999999;
            for(var k = i + 1; k < j; k++)
                dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k][j] + a[i] * a[k] * a[j]);
        }
    return dp[0][n];
}

function main(n)
{
    a[0] = parseInt(document.getElementById("aL1").value);
    for(var i = 1; i <= n; i++)
    {
        a[i] = parseInt(document.getElementById("aR" + i).value);
    }
    for(var i = 0; i <= n; i++)
    {
        dp[i] = new Array();
        for(var j = 0; j <= n; j++)
        {
            dp[i][j] = 0;
        }
    }
    solve(n);
    printG(0, n);
    document.getElementById("ans").innerHTML = dp[0][n];
    document.getElementById("print").innerHTML = "连乘顺序：<br>" + ans;
}

function createInput(n)
{
    var s = "";
    for(var i = 1; i <= n; i++)
    {
        s += "<input id = \"aL" + i + "\"" + "type = \"number\" min = \"1\" max = \"100000000\" placeholder=\"第" + i + "个矩阵行数\" required></input>";
        s += "<label> * </label>"
        s += "<input id = \"aR" + i + "\"" + "type = \"number\" min = \"1\" max = \"100000000\" placeholder=\"第" + i + "个矩阵列数\" required></input>";
        s += "<br>"
    }
    s += "<p><input type = \"submit\" value = \"submit\" onclick = \"main(" + n +  ")\"></input></p>"
    return s;
}

function inputN()
{
    var tmp = parseInt(document.getElementById("N").value);
    if(isNaN(tmp) || tmp < 2 || tmp > 999)
    {
        alert("必须是整数且(2 <= N < 1000)")
    }
    else
    {
        document.getElementById("arrayA").innerHTML = createInput(tmp);
    }
}