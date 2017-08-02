#!usr/bin/python3
# -*- coding:utf-8 -*-
# Filename : .py
# Author by : Lily
"""
分析对比，正则，beautifulsoup,lxml三种抓取数据方式的效率
"""
import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup
import lxml.html
import time
import cssselect


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
#  不用数据需要用到的id属性
fields = ['area', 'population', 'iso', 'country', 'capital', 'continent', 'tld',
          'currency_code', 'currency_name', 'phone', 'postal_code_format',
          'postal_code_regex', 'languages', 'neighbours']


def re_(html):
    for field in fields:
        re.search('<tr id "places_%s__row".*?<td class="w2p_fw">(.*?)</td>' % field, html)


def bs4_(html):
    soup = BeautifulSoup(html, 'html.parser')
    for field in fields:
        soup.find('table').find('tr', id='places_%s__row' % field).find('td', class_='w2p_fw').text


def lxml_(html):
    tree = lxml.html.fromstring(html)
    for field in fields:
        tree.cssselect('table > tr#places_%s__row > td.w2p_fw' % field)[0].text_content()


for name, scrapy in ('re', re_), ('bs4', bs4_), ('lxml_', lxml_):
    # 获取当前时间
    start = time.time()
    # 为了体现明显的区别，循坏1000次
    for i in range(1000):
        # 正则会缓存，缓存会提高效率
        if scrapy == re_:
            re.purge()
            # 清除缓存
        result = scrapy(html)
    end = time.time()
    print('%s:%.2f seconds' % (name, end - start))
