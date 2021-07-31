#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/4/10 13:11
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 40.py
# @Software: PyCharm
# @Desc    : 练习实例40

if __name__ == '__main__':
    lists = [23, 43, 54, 234, 3, 5, 9]
    print("逆序前")
    print(lists)
    size = len(lists)
    for i in range(len(lists) // 2):
        lists[i], lists[size - i - 1] = lists[size - i - 1], lists[i]
    print("逆序后")
    print(lists)
