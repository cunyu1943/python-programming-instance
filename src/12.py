#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/3/31 19:50
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 12.py
# @Software: PyCharm
# @Desc    : 练习实例12

import math

if __name__ == '__main__':
    flag = False
    count = 0
    for i in range(101, 201):
        for j in range(2, int(math.sqrt(i + 1)) + 1):
            if i % j == 0:
                flag = True
                break
        if not flag:
            count += 1
            print(i, end='\t')
            if count % 5 == 0:
                print()
        flag = False
