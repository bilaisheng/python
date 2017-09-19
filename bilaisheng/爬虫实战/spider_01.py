'''
    第一个实例:简单的网页爬虫

    爬去豆瓣首页
'''

import urllib.request

# 网址
url = "http://www.douban.com"

# 请求
request = urllib.request.Request(url)

# 爬取结果
response = urllib.request.urlopen(request)

data = response.read()

# 设置解码方式
data = data.decode('utf-8')

# 打印结果
print(data)


# 打印爬去网页的各类信息
print('===============')
print(type(response))
print('===============')
print(response.geturl())
print('===============')
print(response.info())
print('===============')
print(response.getcode())