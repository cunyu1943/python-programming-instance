#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/4/10 20:53
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 49.py
# @Software: PyCharm
# @Desc    : 练习实例49

if __name__ == '__main__':
    add = lambda num1, num2: num1 + num2
    mul = lambda num1, num2: num1 * num2

    num1 = int(input("输入 num1 \n"))
    num2 = int(input("输入 num2 \n"))
    result1 = add(num1, num2)
    print("num1 + num2 = %d" % add(num1, num2))
    print("num1 * num2 = %d" % mul(num1, num2))
