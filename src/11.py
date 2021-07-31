#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/3/31 19:48
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 11.py
# @Software: PyCharm
# @Desc    : 练习实例11

def rabbit_num(month):
    if month == 1 or month == 2:
        return 1
    else:
        return rabbit_num(month - 2) + rabbit_num(month - 1)


if __name__ == '__main__':

    while True:
        month = input('输入第几个月')
        if month.isdigit():
            month = int(month)
            print('第 %d 个月的兔子数为 %d 对' % (month, rabbit_num(month)))
        elif month == 'q':
            break
        else:
            print('输入错误，请重新输入')
