#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/3/27 12:00
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 1.py
# @Software: PyCharm
# @Desc    : 练习实例1

if __name__ == '__main__':
    # 可组成数的个数
    count = 0

    for i in range(1, 5):
        for j in range(1, 5):
            if i != j:
                for k in range(1, 5):
                    if j != k and i != k:
                        print(str(i) + str(j) + str(k))
                        count += 1

    print("组成的数共有：%d 个" % count)
