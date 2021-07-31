#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/4/10 9:32
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 23.py
# @Software: PyCharm
# @Desc    : 练习实例23

if __name__ == '__main__':
    for i in range(4):
        for j in range(2 - i + 1):
            print(" ", end='')
        for k in range(2 * i + 1):
            print("*", end='')
        print()

    for i in range(3):
        for j in range(i + 1):
            print(" ", end='')
        for k in range(4 - 2 * i + 1):
            print("*", end='')
        print()
