#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/3/31 19:52
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 14.py
# @Software: PyCharm
# @Desc    : 练习实例14

def prime(n):
    print(str(n) + ' = ')
    if not isinstance(n, int) or n <= 0:
        print('Please input a valid number !')
        exit(0)
    elif n in [1]:
        print(n)
    while n not in [1]:
        for index in range(2, int(n + 1)):
            if n % index == 0:
                n /= index
                if n == 1:
                    print(index)
                else:
                    print(str(index) + " *", end=' ')
                break


if __name__ == '__main__':
    num = input('Input the num, enter "q" to quit：')
    while num != 'q':
        prime(int(num))
        num = input('Input the num：')
