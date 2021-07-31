#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/4/10 10:30
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 30.py
# @Software: PyCharm
# @Desc    : 练习实例30

if __name__ == '__main__':
    num = int(input("输入一个 5 位的正整数\n"))
    one = num % 10
    ten = num % 100 // 10
    hundred = num % 1000 // 100
    thousand = num % 10000 // 1000
    million = num // 10000

    if one == million and ten == thousand:
        print("%d 是一个回文数" % num)
    else:
        print("%d 不是一个回文数" % num)
