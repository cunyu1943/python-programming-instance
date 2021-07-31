#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/4/10 10:02
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 25.py
# @Software: PyCharm
# @Desc    : 练习实例25

if __name__ == '__main__':
    sum = 0
    tmp = 1
    for i in range(1, 21):
        tmp *= i
        sum += tmp
    print('1! + 2! + 3! + ... + 20! = ' + str(sum))
