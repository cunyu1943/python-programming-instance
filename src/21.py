#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/3/31 20:42
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 21.py
# @Software: PyCharm
# @Desc    : 练习实例21

if __name__ == '__main__':
    end = 1
    start = 0
    for day in range(10, 1, -1):
        start = (end + 1) * 2
        end = start

    print('第一天的桃子：' + str(start))
