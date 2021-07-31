#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/3/31 20:01
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 17.py
# @Software: PyCharm
# @Desc    : 练习实例17

import string

if __name__ == '__main__':

    s = input('请输入字符串:\n')
    num_letter = 0
    num_space = 0
    num_digit = 0
    num_other = 0

    for i in range(len(s)):
        if s[i].isspace():
            num_space += 1
        elif s[i].isdigit():
            num_digit += 1
        elif s[i].isalpha():
            num_letter += 1
        else:
            num_other += 1

    print('character: ', num_letter)
    print('space: ', num_space)
    print('digit: ', num_digit)
    print('other: ', num_other)
