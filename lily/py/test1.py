# -*- coding:utf-8 -*-
from down import download5
import re
from urllib.parse import urljoin
import urllib.robotparser
import datetime
import urllib.request
import time
from time import sleep
import queue

def get_links(html):
    website_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
    return website_regex.findall(html)

# url = 'http://www.baidu.com'
# html = download5(url)
# links = get_links(html.decode('utf-8'))
# print(links)


def link_crawler1(seed_url,link_regex):
    crawl_queue = [seed_url]
    while crawl_queue:
        url = crawl_queue.pop()
        html = download5(url)
        for link in get_links(html.decode('utf-8')):
            if re.match(link_regex,link):
                crawl_queue.append(link)


def link_crawler2(seed_url,link_regex):
    crawl_queue = [seed_url]
    while crawl_queue:
        url = crawl_queue.pop()
        html = download5(url)
        for link in get_links(html.decode('utf-8')):
            if re.match(link_regex,link):
                link = urljoin(seed_url,link)
                crawl_queue.append(link)


def link_crawler3(seed_url,link_regex):
    crawl_queue = [seed_url]
    seen =set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        html = download5(url)
        for link in get_links(html.decode('utf-8')):
            if re.match(link_regex,link):
                link = urljoin(seed_url,link)
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)


def get_robots(url):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(urljoin(url,'robots.txt'))
    rp.read()
    return rp

def same_domain(url1,url2):
    return urllib.request.urlparse(url1).netloc ==urllib.request.urlparse(url2).netloc

def normalize(seed_url,link):
    link,_ = urllib.urlparse.defrag(link)


class Throttle:
    # 保存数据状态
    # 保存链接的访问时间
    def __init__(self,delay):
        self.delay = delay #休眠时间
        self.domians = {} #和链接对应起来构成字典类型

    def wait(self,url):
        domain = urllib.request.urlparse(url).netloc
        # 链接的主域名
        last_accessed = self.domians.get(domain)
        # 这个链接上一回访问的时间是多少
        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.datetime.now() - last_accessed).seconds
            # 休眠时间  我们设置的休眠时间 - 当前时间减去上一次访问时间 =sleep
            # 间隔时间 （datetime.now() - last_accessed)
            if sleep_secs > 0:

                print('sleep...')
                sleep(sleep_secs)
        self.domians[domain] = datetime.datetime.now()
        # 保存第一次访问后的时间


def link_crawler4(seed_url,link_regex,proxy=None,max_depth = -1,delay = -1,user_agent ='test',num_retries=2):
    # crawl_queue = [seed_url]
    # seen =set(crawl_queue)
    crawl_queue = queue.deque([seed_url])
    seen = {seed_url:0}
    rp = get_robots(seed_url)
    # num = 0
    throttle = Throttle(delay)

    while crawl_queue:
        url = crawl_queue.pop()
        if rp.can_fetch(user_agent,url):
            # if num % 2==0:
            #     sleep(2)
            #     print('sleep now...')
            throttle.wait(url)
            html = download5(url,user_agent=user_agent,proxy =proxy)
            # num += 1
            depth = seen[url]
            if depth != max_depth:
                for link in get_links(html.decode('utf-8')):
                    if re.match(link_regex,link):
                        link = urljoin(seed_url,link)

                        if link not in seen:
                            seen[link] = depth + 1
                            # seen.add(link)
                            if same_domain(seed_url,link):
                                crawl_queue.append(link)
        else:
            print('blocked by robots.txt',url)


url = 'http://example.webscraping.com'
link_crawler4(url,'/places/default/(index|view)',delay =2,max_depth=1)


# url = 'http://www.baidu.com'
# html = download5(url)
# print(get_links(html.decode('utf-8')))
# link_crawler3(url,'http://www.')

