# -*- coding=utf-8 -*-
# Filename : download.py
# Author by : Lily
"""
下载网页内容
"""
# 导入urllib.request库
import urllib.request

# 定义下载页面的方法：版本一
# 用urllib.request.urlopen().read()读取网页内容


def download(url):
    return urllib.request.urlopen(url).read()

# 定义下载页面的方法：版本二
# 下载网页内容，网页异常时返回None


def download2(url):
    print("download2...")
    # 用try...except 捕获错误异常
    try:
        # urlopen()打开网页；read()读取网页内容
        html2 = urllib.request.urlopen(url).read()
    # 捕获URLError，返回None
    except urllib.request.URLError as e:
        print("download error")
        html2 = None
    return html2

# 下载页面内容，版本三
# 下载页面内容，页面异常时重新加载
# num_retries=2 给重新加载的次数默认值


def download3(url, num_retries=2):
    print('download3...')
    try:
        html3 = urllib.request.urlopen(url).read()
    except urllib.request.URLError as e:
        print('download3 error %s' % e.reason)
        html3 = None
        # 当重新加载的次数大于0时
        if num_retries > 0:
            # 当e.code的值在500-600之间时，重新加载页面
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # 调用自身函数
                html3 = download3(url, num_retries-1)
    return html3

# 下载网页内容，版本4
# 设置用户代理


url2 = 'http://www.baidu.com'
url1 = 'http://httpstat.us/500'
html = download3(url2)



print(html)


