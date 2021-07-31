#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/4/10 13:34
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 43.py
# @Software: PyCharm
# @Desc    : 练习实例43

class Num:
    nNum = 1

    def inc(self):
        self.nNum += 1
        print('nNum = %d' % self.nNum)


if __name__ == '__main__':
    nNum = 2
    inst = Num()
    for i in range(3):
        nNum += 1
        print('The num = %d' % nNum)
        inst.inc()
