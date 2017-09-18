#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Filename: 判断奇偶数.py
# Author by : Lily
# 输入一个数字，判断这个数字是奇数还是偶数
# 思路：输入数字，判断是否为数字，不为数字重新输入，若为数字，则判断是奇数还是偶数，输出结果


def is_odd():
    try:
        num = int(input('请输入数字：'))
        if num % 2 == 0:
            print('你输入的%s数偶数' % num)
        else:
            print('你输入的%s是奇数' % num)
    except ValueError:
        print('你输入的不是数字，请重新输入：')
        is_odd()

is_odd()
