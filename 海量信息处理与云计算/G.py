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
    data = {0:[], 1:[]}
    for ds in dataSet:
        data[ds[0]].append(list(map(float, ds[1:])))

    c = (
        Parallel(init_opts=opts.InitOpts(width = "4444px", height = "666px"))
        #下面是暗黑主题
        #Parallel(init_opts=opts.InitOpts(width = "3000px", height = "800px", theme=ThemeType.CHALK))
        .add_schema(
            [
                {"dim": 0, "name": "年龄"},
                {"dim": 1, "name": "身高"},
                {"dim": 2, "name": "体重"},
                {"dim": 3, "name": "细胞内液"},
                {"dim": 4, "name": "细胞外液"},
                {"dim": 5, "name": "肌肉重"},
                {"dim": 6, "name": "蛋白质"},
                {"dim": 7, "name": "瘦体重"},
                {"dim": 8, "name": "无机盐"},
                {"dim": 9, "name": "脂肪重"},
                {"dim": 10, "name": "脂肪百分比"},
                {"dim": 11, "name": "腰臀比"},
                {"dim": 12, "name": "肥胖度"},
                {"dim": 13, "name": "体质指数"},
                {"dim": 14, "name": "肌肉控制"},
                {"dim": 15, "name": "脂肪控制"},
                {"dim": 16, "name": "体重控制"},
                {"dim": 17, "name": "标准体重"},
                {"dim": 18, "name": "目标体重"},
                {"dim": 19, "name": "基础代谢率"},
                {"dim": 20, "name": "躯干肌肉"},
                {"dim": 21, "name": "躯干骨质"},
                {"dim": 22, "name": "躯干脂肪"},
                {"dim": 23, "name": "躯干脂肪百分比"},
                {"dim": 24, "name": "左上肢肌肉"},
                {"dim": 25, "name": "左上肢骨质"},
                {"dim": 26, "name": "左上肢脂肪"},
                {"dim": 27, "name": "右上肢肌肉"},
                {"dim": 28, "name": "右上肢骨质"},
                {"dim": 29, "name": "右上肢脂肪"},
                {"dim": 30, "name": "左下肢肌肉"},
                {"dim": 31, "name": "左下肢骨质"},
                {"dim": 32, "name": "左下肢脂肪"},
                {"dim": 33, "name": "右下肢肌肉"},
                {"dim": 34, "name": "右下肢骨质"},
                {"dim": 35, "name": "右下肢脂肪"}
            ]
        )
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
    parallel_base(pd.read_excel("学生体测数据.xlsx", index_col = 0).values.tolist()).render("学生体侧数据可视化(平行坐标).html")

