#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/4/10 13:24
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 41.py
# @Software: PyCharm
# @Desc    : 练习实例41

class Demo:
    static_value = 10

    def addStatic(self):
        self.static_value += 1
        print(self.static_value)


if __name__ == '__main__':
    demo = Demo()
    for i in range(5):
        demo.addStatic()
