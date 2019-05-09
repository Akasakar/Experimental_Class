# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: C3.6.3.py
# Created:  2019.05.09(UTC+0800)22.00.41(星期四)
'''


from pyecharts import options as opts
from pyecharts.charts import Page, Radar
import math

def radar_base() -> Radar:
    rl = []
    with open("Ex3.6.3.csv", "r") as f:
        rL = f.read().split("\n")

    data = []
    for i in range(1, len(rL) - 1):
        data.append(rL[i].split(","))

    c = (
        Radar()
        .add_schema(
            schema=[
                opts.RadarIndicatorItem(name="Violent", max_=1000),
                opts.RadarIndicatorItem(name="Property", max_=5000),
                opts.RadarIndicatorItem(name="Murder", max_=20),
                opts.RadarIndicatorItem(name="Rape", max_=100),
                opts.RadarIndicatorItem(name="Robbery", max_=500),
                opts.RadarIndicatorItem(name="Assault", max_=1000),
                opts.RadarIndicatorItem(name="Burglary", max_=1000),
                opts.RadarIndicatorItem(name="Larceny", max_=3000),
                opts.RadarIndicatorItem(name="Auto", max_=1000),
                opts.RadarIndicatorItem(name="Inmates", max_=1000),
            ]
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            legend_opts=opts.LegendOpts(selected_mode="single"),
            title_opts=opts.TitleOpts(title="2014年美国各州犯罪率")
            )
    )
    for i in range(len(data)):
        c.add(data[i][0], [list(map(float, data[i][1:]))])

    return c

radar_base().render("Ex3.6.3.html")
