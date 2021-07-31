#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/4/10 9:58
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 24.py
# @Software: PyCharm
# @Desc    : 练习实例24

if __name__ == '__main__':
    numerator = 2
    denominator = 1
    sum = 0
    for i in range(1, 21):
        sum += numerator * 1.0 / denominator
        tmp = numerator
        numerator += denominator
        denominator = tmp
    print('数列之和：' + str(sum))
