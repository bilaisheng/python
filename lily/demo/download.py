# -*- coding=utf-8 -*-
# Filename : download.py
# Author by : Lily
"""
下载网页内容
异常捕获；用户代理；
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
        print("download error", e.reason)
        html2 = None
    return html2

# 下载页面内容，版本三
# 下载页面内容，页面异常时重新加载
# num_retries=2 给重新加载的次数默认值


def download3(url, num_retries=2):
    print('download3...')
    try:
        # urlopen()打开网页；read()读取网页内容
        html3 = urllib.request.urlopen(url).read()
    # 捕获URLError，返回None
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


def download4(url, user_agent='test', num_retries=2):
    print("download4...", url)
    # 设置header 中的用户代理，默认值是test
    headers = {'User_agent': user_agent}
    # 将用户代理添加到请求中
    request = urllib.request.Request(url, headers=headers)
    try:
        # urlopen()打开网页；read()读取网页内容
        html4 = urllib.request.urlopen(request).read()
    # 捕获URLError，返回None
    except urllib.request.URLError as e:
        print("download Error", e.reason)
        html4 = None
        # 当重新加载的次数大于0时
        if num_retries > 0:
            # 当e.code的值在500-600之间时，重新加载页面
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # 调用自身函数
                html4 = download4(url, user_agent, num_retries-1)
    return html4

# 下载网页内容，版本4
# 设置用户代理IP,proxy,代理IP;data是用户可输入的参数


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

# 百度首页
url2 = 'http://www.baidu.com'

# 错误页面 code=500
url1 = 'http://httpstat.us/500'

# 下载百度首页，设置用户代理为360浏览器
html = download4(url2, user_agent='"360":"User-Agent: Mozilla/4.0 (compatible; MS IE 7.0;Window NT 5.1;360SE)"')

# 下载百度首页，设置用户代理为UC浏览器
html1 = download4(url2, user_agent='"UC":"User-Agent:UC WEB7.0.2.37/28/999"')

# 打开pc.html,如路径中无此文件会自动创建
first_file = open('pc.html', "w+", encoding="utf-8")

# 打开mb.html,如果路径中无此文件会自动创建
your_file = open("mb.html", "w+", encoding="utf-8")

# 将下载到的内容写入pc.html(使用360代理)
first_file.write(html.decode("utf-8"))

# 将下载到的内容写入mb.html（使用UC代理）
your_file.write(html1.decode("utf-8"))

# 设置 IP代理
proxy = '117.90.5.133:9000'

# 打印 使用代理IP下载的页面
print(download5(url2, proxy))
