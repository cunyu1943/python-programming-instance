#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/3/31 19:35
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 6.py
# @Software: PyCharm
# @Desc    : 练习实例6

if __name__ == '__main__':
    def fib(num):
        if num <= 2:
            result = 1
        else:
            result = fib(num - 1) + fib(num - 2)
        return result


    while True:
        num = int(input('num = '))
        print('斐波那契数列的第 %d 个值是 %d' % (num, fib(num)))
