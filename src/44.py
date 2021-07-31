#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/4/10 20:35
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 44.py
# @Software: PyCharm
# @Desc    : 练习实例44

if __name__ == '__main__':
    X = [[12, 7, 3],
         [4, 5, 6],
         [7, 8, 9]]

    Y = [[5, 8, 1],
         [6, 7, 3],
         [4, 5, 9]]

    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    for i in range(len(X)):
        for j in range(len(X[0])):
            result[i][j] = X[i][j] + Y[i][j]

    print(result)
