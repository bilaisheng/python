# !/usr/bin/python3
# -*- coding: UTF-8 -*-
import urllib.request


def download5(url, free_proxy=None, user_agent='test', num_retries=2, data=None):
    headers = {
                  "Accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, * / *;q = 0.8",
                  # "Accept-Encoding": "gzip, deflate",
                  "Accept - Language": "zh - CN, zh;q = 0.8, en - us;q = 0.6, en;q = 0.5;q = 0.4",
                  "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 micromessage/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.901.400 QQBrowser/9.0.2524.400"}
    request = urllib.request.Request(url, data, headers=headers)
    opener = urllib.request.build_opener()
    if free_proxy:
        proxy_params = {urllib.request.urlparse(url).scheme: free_proxy}
        opener.add_handler(urllib.request.ProxyHandler(proxy_params))
    try:
        html5 = opener.open(request).read()
    except urllib.request.URLError as e:
        print("download error", e.reason)
        html5 = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                html5 = download5(url, free_proxy, user_agent, num_retries - 1)
    return html5
url = 'http://wx.sephora.cn/index.php?m=Nearby&a=index&provinceid=2&cityid=500'
html = download5(url)

print(html)