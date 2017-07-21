# !/usr/bin/python3
# -*- coding: UTF-8 -*-

# Filename : url_test.py
# Author by : Lily
# 知识点：type();dir();headers();geturl();info();getcode();read()

import urllib.request

html = urllib.request.urlopen('https://taobao.com')

print(type(html))

print(dir(html))

print(html.geturl())

# 返回url的response信息
print(html.headers)

# 返回协议信息的内容
print(html.info())

# 和headers一样
print(html.getcode())

# 返回状态码 通常为200 表示返回成功
# 404 没有找到该网址
print(html.read())
# 打印返回的网页内容
