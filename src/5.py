#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/3/31 19:32
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 5.py
# @Software: PyCharm
# @Desc    : 练习实例5

if __name__ == '__main__':
    while True:
        print('Input x, y, z:')
        arr = []
        for i in range(3):
            tmp = int(input())
            arr.append(tmp)
        arr.sort()
        print('三个数从小到大排序: ', arr)
