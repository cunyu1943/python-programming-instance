#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/4/10 10:19
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 29.py
# @Software: PyCharm
# @Desc    : 练习实例29

if __name__ == '__main__':
    num = int(input("输入一多于 5 位的正整数\n"))
    one = num % 10
    ten = num % 100 // 10
    hundred = num % 1000 // 100
    thousand = num % 10000 // 1000
    million = num // 10000

    if million != 0:
        print("5 位数：", one, ten, hundred, thousand, million)
    elif thousand != 0:
        print("4 位数：", one, ten, hundred, thousand)
    elif hundred != 0:
        print("3 位数：", one, ten, hundred)
    elif ten != 0:
        print("2 位数：", one, ten)
    elif one != 0:
        print("1 位数：", one)
