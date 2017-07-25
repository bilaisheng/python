''''
    批量下载豆瓣首页的图片

    采用伪装浏览器的方式爬去豆瓣网站首页的图片,保存到指定路径你文件夹下
'''

import urllib.request
import re
import ssl
import os


# 用if __name__ = '__main__' 来判断是否执行该文件

# 定义保存文件的路径
targetPath = "F:\\Spider\\03\\images"


def save_file(path):
    # 检测当前路径的有效性
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)

    # 设置每个图片的路径,获取最后一个 '/'的位置
    position = path.rindex('/')
    # 图片文件路径
    filepath = os.path.join(targetPath, path[position+1:])

    return filepath


# 使用ssl创建未经验证的上下文，在urlopen中传入上下文参数
context = ssl._create_unverified_context()

# 网址
url = "http://www.douban.com/"

user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"

request = urllib.request.Request(url)

request.add_header("User-Agent", user_agent)

# 若不增加ssl验证(context=context) 程序执行出错
response = urllib.request.urlopen(request, context=context)

data = response.read()


for link, t in set(re.findall(r'(https:[^s]*?(jpg|png|gif))', str(data))):

    print(link)
    try:
        urllib.request.urlretrieve(link, save_file(link))
    except:
        print('link: \t' + link + '失败')
