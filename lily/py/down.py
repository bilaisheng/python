import urllib.request
import urllib.parse


def download(url):
    return urllib.request.urlopen(url).read()


def download2(url):
    print('download...'+url)
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.request.URLError as e:
        print('Download error:'+e.reason)
        html = None
    return html


def download3(url,num_retries=2):
    print('download...',url)
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.request.URLError as e:
        print('Download error:',e.reason)
        html= None
        if num_retries > 0:
            if hasattr(e,'code') and 500 <= e.code < 600:
                html = download3(url,num_retries - 1)
    return html
# http://httpstat.us/500
# download3('http://httpstat.us/500')

# 服务器过载503的错误，我们重新下载 。出现5xx错误的时候重新下载
# 404 not found 压根网站就不存在。出现4XX的返回错误

# 使用代理


def download4(url,user_agent='test',num_retries=2):
    print('download...',url)
    headers = {'User-agent':user_agent}
    request = urllib.request.Request(url,headers=headers)
    try:
        html = urllib.request.urlopen(request).read()
    except urllib.request.URLError as e:
        print('Download error:',e.reason)
        html= None
        if num_retries > 0:
            if hasattr(e,'code') and 500 <= e.code < 600:
                html = download4(url,user_agent,num_retries - 1)
    return html


# IP代理
# 国外网站，普通IP是访问不到的。
# python http模块中的requests


def download5(url1, user_agent='test', num_retries=2, data = None, proxy=None):
    print('download...', url1)
    headers = {'User-agent':user_agent}
    request = urllib.request.Request(url1, data, headers=headers)
    opener = urllib.request.build_opener()
    print(opener)
    if proxy:
        proxy_params = {urllib.parse.urlparse(url1).scheme:proxy}
        opener.add_handler(urllib.request.ProxyHandler(proxy_params))
    try:
        html = opener.open(request).read()
    except urllib.request.URLError as e:
        print('Download error:',e.reason)
        html= None
        if num_retries > 0:
            if hasattr(e,'code') and 500 <= e.code < 600:
                html = download5(url1, user_agent, num_retries - 1, )
    return html

#
# url = 'http://www.baidu.com'
# proxy = '121.232.145.33:9000'
# print(download5(url, proxy1=proxy))

# url = 'http://www.baidu.com'
# html = download5(url,user_agent='"360":"User-Agent: Mozilla/4.0(compatible;MSIE 7.0;Windows NT 5.1;360SE)"')
# html1 = download5(url,user_agent='"UC":"UserAgent:UCWEB7.0.2.37/28/999"')
# ml = open('pc.html', 'w', encoding='utf-8')
# ml1 = open('mb.html', 'a+',encoding='utf-8')
# ml.write(html.decode('utf-8'))
# ml1.write(html1.decode('utf-8'))
# ml.close()
# ml1.close()
# request = urllib.request.Request(url,headers=headers)
# proxy = 'http:192.168.1.1:80'
# opener = urllib.request.build_opener()
# proxy_params ={urllib.parse.urlparse(url).scheme:proxy)
# opener.add_hander(urllib.request.ProxyHandler(proxy_params))
# response = opener.open()
# # scheme 代表使用的http协议

