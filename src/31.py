#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/4/10 10:35
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 31.py
# @Software: PyCharm
# @Desc    : 练习实例31

if __name__ == '__main__':

    letter = input("输入星期几的英文:")

    if letter == 'S':
        print('继续输入第二个字母:')
        letter = input("请输入:")
        if letter == 'a':
            print('星期六：Saturday')
        elif letter == 'u':
            print('星期天：Sunday')
        else:
            print('输入错误')

    elif letter == 'F':
        print('星期五：Friday')

    elif letter == 'M':
        print('星期一：Monday')

    elif letter == 'T':
        print('继续输入第二个字母:')
        letter = input("请输入:")

        if letter == 'u':
            print('星期二：Tuesday')
        elif letter == 'h':
            print('星期四：Thursday')
        else:
            print('输入错误')

    elif letter == 'W':
        print('星期三：Wednesday')
    else:
        print('输入错误')
