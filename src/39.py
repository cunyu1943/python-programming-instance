#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/4/10 12:49
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 39.py
# @Software: PyCharm
# @Desc    : 练习实例39

def sorted_add(lists, num):
    for i in range(len(lists)):
        if lists[i] > num:
            lists.insert(i, num)
            break
        if i == len(lists) - 1:
            lists.append(num)


if __name__ == '__main__':
    lists = [1, 4, 5, 6, 9, 19]
    print("加入前")
    print(lists)

    num = int(input("\n输入你要加入的数\n"))
    sorted_add(lists, num)
    print("加入后")
    print(lists)
