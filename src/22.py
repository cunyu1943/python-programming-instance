#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/3/31 20:45
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 22.py
# @Software: PyCharm
# @Desc    : 练习实例22

if __name__ == '__main__':
    for i in range(ord('x'), ord('z') + 1):
        for j in range(ord('x'), ord('z') + 1):
            if i != j:
                for k in range(ord('x'), ord('z') + 1):
                    if (i != k) and (j != k):
                        if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                            print('对战名单：\na <-> %s\nb <-> %s\nc <-> %s' % (chr(i), chr(j), chr(k)))
