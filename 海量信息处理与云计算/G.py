# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: G.py
# Created:  2019.06.11(UTC+0800)15.51.54(星期二)
'''

from pyecharts import options as opts
from pyecharts.charts import Parallel
from pyecharts.globals import ThemeType, ChartType, SymbolType
import pandas as pd

def parallel_base(dataSet) -> Parallel:
    schema = [{"dim":i - 1, "name":dataSet[0][i]} for i in range(1, len(dataSet[0]))]
    DS, data = dataSet[1:], {0:[], 1:[]}
    for ds in DS:
        data[ds[0]].append(list(map(float, ds[1:])))

    c = (
        Parallel(init_opts=opts.InitOpts(width = "4444px", height = "666px"))
        #下面是暗黑主题
        #Parallel(init_opts=opts.InitOpts(width = "3000px", height = "800px", theme=ThemeType.CHALK))
        .add_schema(schema)
        .set_global_opts (
            title_opts = opts.TitleOpts(title="学生体侧数据"),
            legend_opts = opts.LegendOpts(is_show = True),
            toolbox_opts = opts.ToolboxOpts(),
        )
    )
    for k in data.keys():
        c.add(str(k), data[k])
    return c


if __name__ == "__main__":
    parallel_base(pd.read_excel("学生体测数据.xlsx", header = None, index_col = 0).values.tolist()).render("学生体侧数据可视化(平行坐标).html")

