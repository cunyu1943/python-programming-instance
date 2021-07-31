#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/3/31 20:03
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 19.py
# @Software: PyCharm
# @Desc    : 练习实例19

if __name__ == '__main__':
    for num in range(2, 1001):
        arr = []
        for i in range(1, num):
            if num % i == 0:
                arr.append(i)
        if sum(arr) == num:
            print(num, arr)
