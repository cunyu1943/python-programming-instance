#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/4/10 11:02
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 36.py
# @Software: PyCharm
# @Desc    : 练习实例36

if __name__ == '__main__':
    count = 0
    for i in range(1, 101):
        if i > 1:
            for j in range(2, i):
                if (i % j == 0):
                    break
            else:
                print(i, end='\t')
                count += 1
                if (count % 5 == 0):
                    print()
    print("共有素数 %d 个" % count)
