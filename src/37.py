#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/4/10 11:09
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 37.py
# @Software: PyCharm
# @Desc    : 练习实例37

if __name__ == '__main__':
    lists = []
    for i in range(10):
        lists.append(int(input("请输入" + str(i + 1) + "个整数\n")))
    print("排序前的数")
    for item in lists:
        print(item, end='\t')

    for i in range(9):
        min = i
        for j in range(i + 1, 10):
            if lists[min] > lists[j]:
                min = j
        tmp = lists[i]
        lists[i] = lists[min]
        lists[min] = tmp
    print("\n排序后的数")
    for item in lists:
        print(item, end='\t')
