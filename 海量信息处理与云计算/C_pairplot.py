# -*- coding: UTF-8 -*-
'''
# Author:   Akasaka
# FileName: Cx.py
# Created:  2019.05.10(UTC+0800)21.01.08(星期五)
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

iris = pd.read_csv('iris.csv')

#散点矩阵图
sns.pairplot(iris, hue = 'species',)
plt.show()

#平行坐标图
_, axes = plt.subplots()
parallel_coordinates(iris, 'species',ax = axes)
plt.show()
