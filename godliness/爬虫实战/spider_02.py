'''
    伪装浏览器

    对于一些需要登录的网站,如果不是从浏览器发出的请求,则得不到响应
    所以,我们需要将爬虫程序发出的请求伪装成浏览器正规军
    具体时间:自定义网页请求报文头

'''

# 实例二: 依然爬取豆瓣 采用伪装浏览器的方式

import urllib.request


# 定义保存函数
def save_file(data):
    path = "F:/Spider/02_douban.out"
    f = open(path, 'wb')
    f.write(data)
    f.close()
