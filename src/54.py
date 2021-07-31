#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/4/10 21:25
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 54.py
# @Software: PyCharm
# @Desc    : 练习实例54

if __name__ == '__main__':
    num1 = int(input("输入：\n"))
    num2 = num1 >> 4
    num3 = ~(~0 << 4)
    num4 = num2 & num3
    print('%o\t%o' % (num1, num4))
