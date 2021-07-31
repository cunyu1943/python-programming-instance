#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/3/27 13:38
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 3.py
# @Software: PyCharm
# @Desc    : 练习实例3

if __name__ == '__main__':

    res = 168 // 2
    for i in range(1, res + 1):
        if 168 % i == 0:
            j = 168 / i
            if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
                m = (i + j) / 2
                n = (i - j) / 2
                x = m * m - 268
                print('这个数可能是: ', x)
