#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/4/10 10:07
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 26.py
# @Software: PyCharm
# @Desc    : 练习实例26

def fact(num):
    if num == 0:
        return 1
    else:
        return fact(num - 1) * num


if __name__ == '__main__':
    print(fact(5))
