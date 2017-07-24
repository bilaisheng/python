'''
    伪装浏览器

    对于一些需要登录的网站,如果不是从浏览器发出的请求,则得不到响应
    所以,我们需要将爬虫程序发出的请求伪装成浏览器正规军
    具体时间:自定义网页请求报文头

'''

# 实例二: 依然爬取豆瓣 采用伪装浏览器的方式
import ssl
import urllib.request


# 定义保存函数
def save_file(data):
    # 此处自行创建目录 , 文件
    path = "F:/Spider/02_douban.out"
    f = open(path, 'wb')
    f.write(data)
    f.close()

# 使用ssl创建未经验证的上下文，在urlopen中传入上下文参数
context = ssl._create_unverified_context()

# 网址
url = "http://www.douban.com/"

user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"


request = urllib.request.Request(url)

request.add_header("User-Agent", user_agent)

# 若不增加ssl验证 程序执行出错
response = urllib.request.urlopen(request, context=context)


data = response.read()

# 把爬取的内容保存到文件中
save_file(data)

data.decode('utf-8')
# 打印抓取的内容
print(data)