#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/4/10 10:40
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 33.py
# @Software: PyCharm
# @Desc    : 练习实例33

if __name__ == '__main__':
    lists = [1, 3, 4, 5, 6]

    for i in range(len(lists)):
        if i == len(lists) - 1:
            print(lists[i], end='')
        else:
            print(lists[i], end=',')
