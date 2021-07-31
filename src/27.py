#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/4/10 10:09
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 27.py
# @Software: PyCharm
# @Desc    : 练习实例27

def reverseString(str, length):
    if (length == 0):
        return
    print(str[length - 1], end='')
    reverseString(str, length - 1)


if __name__ == '__main__':
    str = input("输入字符串\n")
    reverseString(str, len(str))
