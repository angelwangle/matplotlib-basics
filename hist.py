# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 21:00:53 2020

@author: User
"""

import matplotlib.pyplot as plt
# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

types = ('原图', '攻击失败', '对抗样本', '防御成功', '前M(150)','前N(10)','前K(2)')
number = [166, 23, 143, 76, 135, 102, 87]

plt.bar(types, number, width = 0.6, color = '#808080')
plt.ylabel('图片数量') 
for x, y in zip(types, number):
    plt.text(x, y, str(y), ha = 'center', va = 'bottom')      
plt.savefig('D:/plot.svg')
plt.show()