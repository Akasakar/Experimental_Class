# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: C3.6.4.py
# Created:  2019.05.09(UTC+0800)22.01.35(星期四)
'''


from pyecharts import options as opts
from pyecharts.charts import Page, Parallel
from pyecharts.globals import ThemeType

help(ThemeType)
def parallel_base() -> Parallel:
    rL = []
    with open("iris.data", "r") as f:
        rL = f.read().split("\n")
    nameSet, data = set(), {}
    for i in range(len(rL) - 1):
        tmp = rL[i].split(",")
        if tmp[-1] not in nameSet:
            nameSet.add(tmp[-1])
            data[tmp[-1]] = []
        data[tmp[-1]].append(list(map(float, tmp[:-1])))

    c = (
        Parallel(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add_schema(
            [
                {"dim": 0, "name": "calyx length"},
                {"dim": 1, "name": "calyx width"},
                {"dim": 2, "name": "petal length"},
                {"dim": 3, "name": "petal width"},
            ]
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="鸢尾花数据集"))
    )

    for k in data.keys():
        c.add(k, data[k])
    return c

parallel_base().render("Iris.html")

