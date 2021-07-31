#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/3/31 19:51
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 13.py
# @Software: PyCharm
# @Desc    : 练习实例13

if __name__ == '__main__':
    print('水仙花数列表:')
    for i in range(100, 1000):
        ge = i % 10
        shi = i // 10 % 10
        bai = i // 100

        if i == (ge ** 3 + shi ** 3 + bai ** 3):
            print(i)
