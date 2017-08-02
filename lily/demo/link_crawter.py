#!usr/bin/python3
# -*- coding:utf-8 -*-
# Filename : link_crawter.py
# Auther by : Lily
"""
获取一个网站所有的链接
"""
import datetime
from collections import deque
from time import sleep
import urllib.parse
from download_quote import download5
import re
import urllib.request
import urllib.robotparser
from bs4 import BeautifulSoup
# 获取网站中的所有链接，从所有a标签中获取href属性中的内容


def get_link(html):
    # 提取所有a标签中获取href属性中的内容
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # 返回所有获取到的内容
    return webpage_regex.findall(html)


# 获取robots.txt文件
def get_robots(url):
    # 创建RobotFileParser句柄
    rp = urllib.robotparser.RobotFileParser()
    # 在句柄中添加url参数
    rp.set_url(urllib.parse.urljoin(url, '/robots.txt'))
    # 读取句柄内容
    rp.read()
    # 返回 句柄内容
    return rp


# 获取链接的正常部分(不包含参数)
def normalize(seed_url, link):
    link, _ = urllib.parse.urldefrag(link)
    return urllib.parse.urljoin(seed_url, link)


# 判断抓取的链接的主链接是否是我们要抓取的主链接
def same_domain(url1, url2):
    return urllib.request.urlparse(url1).netloc == urllib.request.urlparse(url2).netloc


# 提取所有有用的链接；seed_url网页url;link_regex链接匹配的正则表达式
# 如果获取的链接不是全的链接，将会报错


def link_crawler(seed_url, link_regex):
    # 将网页链接传给craw_queue
    craw_queue = [seed_url]
    # 遍历craw_queue所有的值
    while craw_queue:
        # 删除craw_queue的最后一个值，并返回给url
        url = craw_queue.pop()
        # download url的网页内容
        html = download5(url).decode('utf-8')
        # 在html页面中获取所有的链接
        for link in get_link(html):
            # 判断link是否满足link_regex正则表达式；如果满足则添加到craw_queue中
            if re.match(link_regex, link):
                # 在craw_queue中添加link
                craw_queue.append(link)

# 提取所有有用的链接；seed_url网页url;link_regex链接匹配的正则表达式
# 获取的链接都是缺少主链接的子链接，需要合并成完整的链接
# 如果有链接是重复的会访问多次


def link_crawler2(seed_url, link_regex):
    # 将网页链接传递给craw_queue
    craw_queue = [seed_url]
    # 遍历craw_queue的所有值
    while craw_queue:
        # 删除craw_queue的最后一个值，并返回给url
        url2 = craw_queue.pop()
        # download url 的网页内容
        html = download5(url2).decode('utf-8')
        # 在html页面中获取所有的链接
        for link in get_link(html):
            # 判断link是否满足link_regex正则表达式；如果满足则添加到craw_queue中
            if re.match(link_regex, link):
                # 将主链接和不全的子链接拼接成完整的链接
                link = urllib.parse.urljoin(seed_url, link)
                # 在craw_queue添加link
                craw_queue.append(link)


# 提取所有有用的链接；seed_url网页url;link_regex链接匹配的正则表达式
# 获取的链接都是缺少主链接的子链接，需要合并成完整的链接
# 如果有链接是重复的会被过滤掉

def link_crawler3(seed_url, link_regex):
    # 将网页链接传递给craw_queue
    craw_queue = [seed_url]
    # 将craw_queue存入set()类型中，目的是去除重复项
    seen = set(craw_queue)
    # 遍历craw_queue的所有值
    while craw_queue:
        # 删除craw_queue的最后一个值，并返回给url
        url3 = craw_queue.pop()
        # download url 的网页内容
        html = download5(url3).decode('utf-8')
        # 在html页面中获取所有的链接
        for link in get_link(html):
            # 判断link是否满足link_regex正则表达式；
            if re.match(link_regex, link):
                # 将主链接和不全的子链接拼接成完整的链接
                link = urllib.parse.urljoin(seed_url, link)
                # 判断link是否在seen中；若不在则添加到seen中；及添加到craw_queue中
                if link not in seen:
                    # 在seen中添加link元素
                    seen.add(link)
                    # 在craw_queue中添加link元素
                    craw_queue.append(link)


# 提取所有有用的链接；seed_url网页url;link_regex链接匹配的正则表达式
# 获取的链接都是缺少主链接的子链接，需要合并成完整的链接
# 如果有链接是重复的会被过滤掉
# 将robots分析功能添加到代码中
# robots文件中表示了你的用户代理可以访问哪些路由


def link_crawler4(seed_url, link_regex, user_agent='Test'):
    # 将seed_url赋值给craw_queue
    craw_queue = [seed_url]
    # 将craw_queque保存为set()类型
    seen = set(craw_queue)
    # 获取robots文件存到rp
    rp = get_robots(seed_url)
    # 当craw_queue不为空时，执行循环
    while craw_queue:
        # 删除并返回craw_queue的最后一个值
        url4 = craw_queue.pop()
        # 访问一个robots.txt为空的时，返回一直True
        if rp.can_fetch(user_agent, url4):
            # download url4 的网页内容
            html = download5(url4, user_agent=user_agent).decode('utf-8')
            # 在html页面中获取所有的链接
            for link in get_link(html):
                # 判读link是否符合link_regex正则表达式
                if re.match(link_regex, link):
                    # 拼接获取到到link 和seec_url得到完整的链接地址
                    link = urllib.parse.urljoin(seed_url, link)
                    # 判断link是否在seen中
                    if link not in seen:
                        # 在seen中添加一个元素link
                        seen.add(link)
                        # 在craw_queue中添加link
                        craw_queue.append(link)
        else:
            # 如果判读该网页robots不能爬取，则打印 blocked by robots.txt
            print('blocked by robots.txt', url4)


# 提取所有有用的链接；seed_url网页url;link_regex链接匹配的正则表达式
# 获取的链接都是缺少主链接的子链接，需要合并成完整的链接
# 如果有链接是重复的会被过滤掉
# 将robots分析功能添加到代码中
# robots文件中表示了你的用户代理可以访问哪些路由
# 对下载限速
class Throttle:
    # 保存数据状态
    # 保存链接访问时间
    def __init__(self, delay):
        # 休眠时间
        self.delay = delay
        # 和链接对应起来构成字典的数据类型
        self.domains = {}

    def wait(self, url):
        # 获取链接的主域名
        domain = urllib.request.urlparse(url).netloc
        # 这个链接上次访问的时间是多少
        last_assessed = self.domains.get(domain)
        # 判断 延迟时间是否大于0，上次访问时间是否不为空
        if self.delay > 0 and last_assessed is not None:
            # 休眠的时间  我们设置的休眠时间 - 当前时间减去上次访问时间 = sleep
            # 间隔时间
            sleep_secs = self.delay - (datetime.datetime.now() - last_assessed).seconds
            print('sleep...')
            # 如果休眠时间大于0，执行睡眠，时长为sleep_secs
            if sleep_secs > 0:
                sleep(sleep_secs)
        # 保存最后一次访问时间
        self.domains[domain] = datetime.datetime.now()


def link_crawler5(seed_url, link_regex, delay=-1, user_agent='Test'):
    # 将seed_url赋值给craw_queue
    craw_queue = [seed_url]
    # 将craw_queque保存为set()类型
    seen = set(craw_queue)
    # 获取seed_url的robots的内容
    rp = get_robots(seed_url)
    # num = 0
    # 创建Throttle的一个实例
    throttle = Throttle(delay)
    # 当craw_queue不为空时，执行循环
    while craw_queue:
        url5 = craw_queue.pop()
        # 访问一个robots.txt为空的时，返回一直True
        if rp.can_fetch(user_agent, url5):
            # 粗暴的延时方式：
            # if num % 2 == 0:
            #     sleep(2)
            #     print('sleep now...')
            # 执行时间延时函数
            throttle.wait(url5)
            # download url5 的网页内容
            html = download5(url5, user_agent=user_agent).decode('utf-8')
            # num += 1
            # 在html页面中获取所有的链接
            for link in get_link(html):
                # 判读link是否符合link_regex正则表达式
                if re.match(link_regex, link):
                    # 拼接获取到到link 和seec_url得到完整的链接地址
                    link = urllib.parse.urljoin(seed_url, link)
                    # 判断link是否在seen中
                    if link not in seen:
                        # 在seen中添加一个元素link
                        seen.add(link)
                        # 在craw_queue中添加link
                        craw_queue.append(link)
        else:
            # 如果判读该网页robots不能爬取，则打印 blocked by robots.txt
            print('blocked by robots.txt', url5)


# 提取所有有用的链接；seed_url网页url;link_regex链接匹配的正则表达式
# 获取的链接都是缺少主链接的子链接，需要合并成完整的链接
# 如果有链接是重复的会被过滤掉
# 将robots分析功能添加到代码中
# robots文件中表示了你的用户代理可以访问哪些路由
# 对下载限速
# 对抓取页面的深度进行限制,避免爬虫进入爬虫陷阱
# 排除主链接不一致的链接


def link_crawler6(seed_url, link_regex, max_depth=-1, delay=-1, user_agent='Test',num_retries=2):
    # 将seed_url赋值给craw_queue
    # craw_queue = [seed_url]
    # deque双向队列，效率比普通对列高
    craw_queue = deque([seed_url])
    # 新建一个深度字典
    seen = {seed_url: 0}
    # 获取seed_url的robots的内容
    rp = get_robots(seed_url)
    # 创建Throttle的一个实例
    throttle = Throttle(delay)
    # 当craw_queue不为空时，执行循环

    while craw_queue:
        url6 = craw_queue.pop()
        # 访问一个robots.txt为空的时，返回一直True

        if rp.can_fetch(user_agent, url6):
            throttle.wait(url6)
            # download url5 的网页内容
            html = download5(url6, user_agent=user_agent, num_retries=num_retries).decode('utf-8')
            depth = seen[url6]
            links = []
            if depth != max_depth:
                if link_regex:
                    links.extend(link for link in get_link(html) if re.match(link_regex,link))
                    # links里面都是相对链接/places/default/(index|view)
                # 在html页面中获取所有的链接
                for link in get_link(html):
                    # 对链接进行优化
                    link = normalize(seed_url, link)
                    # 判读link是否符合link_regex正则表达式
                    # if re.match(link_regex, link):

                    # 拼接获取到到link 和seec_url得到完整的链接地址
                    # link = urllib.parse.urljoin(seed_url, link)
                    # 判断link是否在seen中
                    if link not in seen:
                        # 在seen中添加一个元素link
                        seen[link] = depth + 1
                        if same_domain(seed_url, link):
                            # 在craw_queue中添加link
                            craw_queue.append(link)
                        else:
                            print(seed_url, link)
        else:
            # 如果判读该网页robots不能爬取，则打印 blocked by robots.txt
            print('blocked by robots.txt', url6)
url = 'http://www.baidu.com'
url1 = 'http://example.webscraping.com/places/default/view/Afghanistan-1'
html = download5(url1).decode("utf-8")
link_crawler6(url1, '/places/default/(index|view)', delay=2, max_depth=2)

