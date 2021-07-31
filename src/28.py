#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/4/10 10:16
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 28.py
# @Software: PyCharm
# @Desc    : 练习实例28

def age(num):
    if num == 1:
        return 10
    else:
        return 2 + age(num - 1)


if __name__ == '__main__':
    print("第五个人的年龄：" + str(age(5)))
