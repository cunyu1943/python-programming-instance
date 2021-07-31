#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/4/10 13:28
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 42.py
# @Software: PyCharm
# @Desc    : 练习实例42


def autofunc():
    num = 1
    print('方法内部 %d' % num)
    num += 1


if __name__ == '__main__':
    num = 10
    for i in range(3):
        print('num = %d' % num)
        num += 1
        autofunc()
