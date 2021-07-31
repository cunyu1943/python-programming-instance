#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/4/10 12:36
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 38.py
# @Software: PyCharm
# @Desc    : 练习实例38


if __name__ == '__main__':
    lists = []
    sum = 0.0

    for i in range(3):
        lists.append([])
        for j in range(3):
            lists[i].append(float(input("输入元素\n")))

    print("这个矩阵是：")
    for i in range(3):
        for j in range(3):
            print(lists[i][j], end='\t')
        print("\n")

    for i in range(3):
        sum += lists[i][i]

    print("主对角线元素和是：" + str(sum))
