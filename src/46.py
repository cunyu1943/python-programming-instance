#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/4/10 20:42
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 46.py
# @Software: PyCharm
# @Desc    : 练习实例46

if __name__ == '__main__':
    while True:
        num = int(input('输入：\n'))
        print('num 的平方：%d' % (num * num))
        if num * num < 50:
            break
