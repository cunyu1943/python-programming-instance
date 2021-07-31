#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/4/10 20:45
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 47.py
# @Software: PyCharm
# @Desc    : 练习实例47

if __name__ == '__main__':
    num1 = 10
    num2 = 20
    print("num1 = %d, num2 = %d" % (num1, num2))
    num1, num2 = num2, num1
    print("num1 = %d, num2 = %d" % (num1, num2))
