#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/4/10 20:45
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 48.py
# @Software: PyCharm
# @Desc    : 练习实例48

if __name__ == '__main__':
    num1 = int(input("输入 num1：\n"))
    num2 = int(input("输入 num2：\n"))

    if num1 > num2:
        print('%d 大于 %d' % (num1, num2))
    elif num1 == num2:
        print('%d 等于 %d' % (num1, num2))
    elif num1 < num2:
        print('%d 小于 %d' % (num1, num2))
