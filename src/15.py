#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/3/31 19:56
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 15.py
# @Software: PyCharm
# @Desc    : 练习实例15

if __name__ == '__main__':
    print('输入成绩查看等级，输入"q"则退出')
    while True:
        score = input('输入你的成绩:')

        if score.isdigit():

            score_rank = int(score) // 10

            if score_rank >= 9:
                print('A')
            elif 6 <= score_rank < 9:
                print('B')
            else:
                print('C')
        elif score == 'q':
            break
        else:
            print('输入错误，请重新输入！')
