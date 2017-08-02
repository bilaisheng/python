#!usr/bin/python3
# -*- coding:utf-8 -*-
# Filename : re_scrap.py
# Author by : Lily
"""
正则表达式抓取内容
"""

import urllib.parse
import re
import urllib.request
import urllib.robotparser


def download5(url, free_proxy=None, user_agent='test', num_retries=2, data=None):
    print("download5...", url)
    # 设置headers 中的用户代理，默认值是test
    headers = {"User_agent": user_agent}
    # 将用户代理添加到请求中
    request = urllib.request.Request(url, data, headers=headers)
    # 创建句柄
    opener = urllib.request.build_opener()
    # 判断如果proxy是否有值
    if free_proxy:
        # 获取ip代理协议和IP代理
        proxy_params = {urllib.request.urlparse(url).scheme: free_proxy}
        # 将IP代理设置添加到句柄中
        opener.add_handler(urllib.request.ProxyHandler(proxy_params))
    try:
        # 使用句柄的open()打开网页，read()读取内容
        html5 = opener.open(request).read()
    # 异常处理，捕获异常
    except urllib.request.URLError as e:
        # 打印异常原因
        print("download error", e.reason)
        html5 = None
        # 判断重新加载次数是否大于0
        if num_retries > 0:
            # 判断 页面code是否在500和600之间
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # 调用自身
                html5 = download5(url, free_proxy, user_agent, num_retries - 1)
    return html5


url1 = 'http://example.webscraping.com/places/default/view/Afghanistan-1'
html = download5(url1).decode("utf-8")
res = re.findall('<tr id="places_area__row".*?<td\s*class=["\']w2p_fw["\']>(.*?)</td>', html)
print(res)

