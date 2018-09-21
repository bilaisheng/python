# coding=utf8
import urllib.request
import json
from urllib import parse


def download5(url, free_proxy=None, user_agent='test', num_retries=2, data=None):
    # print("download5...", url)
    # 设置headers 中的用户代理，默认值是test
    headers = {"User_agent": "Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255"}
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
    return html5.decode('utf-8')
url = "https://www.starbucks.com.cn/api/stores/nearby?lat=39.893781&lon=116.388887&limit=4000&locale=ZH&features=&radius=48302000000"
url_h = "https://www.starbucks.com.cn/api/stores/"
# url = "https://www.starbucks.com.cn/api/stores/1013002?locale=zh"
f = open('Starbucks-s180625-text.csv', "w+", encoding="utf-8")

html = download5(url)
print(type(html))

data = json.loads(html)
print(type(html))
ids = []
for store in data["data"]:
    ids.append(store["id"])

for url_id in ids:
    print(url_id)
    url_detail = url_h + url_id
    html_detail = download5(url_detail)
    html_detail = json.loads(html_detail)
    print(html_detail)
    # for s in html_detail["data"]:
    #     for k,v in s.items():
    #         v = str(v).replace(",", "，")
    #         f.write(str(v))
    #         f.write(',')
    #     f.write('\n')
f.close()