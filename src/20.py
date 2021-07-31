#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/3/31 20:04
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 20.py
# @Software: PyCharm
# @Desc    : 练习实例20

if __name__ == '__main__':
    # 初始距离
    distance = 100

    total = 0

    total += distance

    # 第10次落地时，经历了9次弹起到落地
    for i in range(9):
        distance /= 2
        total += 2 * distance

    print('总共经过距离: ', total)
    print('第10次反弹距离: ', distance / 2)
