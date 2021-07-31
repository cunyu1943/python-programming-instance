#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/3/31 19:40
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 8.py
# @Software: PyCharm
# @Desc    : 练习实例8

if __name__ == '__main__':
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('%d * %d = %d\t' % (i, j, i * j), end=' ')
        print()
