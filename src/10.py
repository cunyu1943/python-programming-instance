#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @version : 1.0
# @Time    : 2021/3/31 19:47
# @Author  : cunyu
# @Email   : 747731461@qq.com
# @Site    : https://cunyu1943.site
# 公众号    : 村雨遥
# @File    : 10.py
# @Software: PyCharm
# @Desc    : 练习实例10

import time

if __name__ == '__main__':
    print('当前时间:')
    print(time.strftime("%Y-%m-%d %H:%M:%S %a", time.localtime()))
    time.sleep(1)
    print('等待一秒后时间:')
    print(time.strftime("%Y-%m-%d %H:%M:%S %a", time.localtime()))
