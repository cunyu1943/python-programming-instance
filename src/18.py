#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/3/31 20:02
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 18.py
# @Software: PyCharm
# @Desc    : 练习实例18

if __name__ == '__main__':
    num = input('输入重复的数字:\n')
    times = int(input('你要重复的次数:\n'))

    answer = 0
    for i in range(times):
        answer += int(num)
        num += num[0]

    print('结果为: ', answer)
