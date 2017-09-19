#!/usr/bin/env python3
# --*-- coding utf-8 --*--
#新建文件utf-8编码，Python3.5.2
# coding:utf-8
__author__ = 'PengRong'

import urllib.request
import re             # regular expression module
import  chardet       # this is for detecting what kind of encoding the web page uses
import urllib.parse   # this module is for scratch the domain name from a url
import itertools
def download(url,user_agent='wsp',number_retries=2):
	print('downloading:'+url)
	headers={'user-agent':user_agent}   # set the user agent in headers
	request=urllib.request.Request(url,headers=headers) # put the headers into the request
	try:
		context = urllib.request.urlopen(request)
		print(context.getcode())
		headers=context.getheaders()
		#headers['Content']
		html=context.read() #<class 'bytes'>,it is a bytes object without decode
		charset=chardet.detect(html)['encoding']  # to detect the encoding method of a page
		print(charset)
		html=html.decode(charset)   # we use the corresponding encoding method to decode the page
		print(html)
		#decode( 'utf-8' )
		print(type(html))  # <class 'str'> after decoding, html becomes strings which can be used directly by regEX
	except urllib.request.URLError as e:
		print('download errors:',e.reason)
		html=None
		if number_retries>0:                      # HTTP-500内部服务器错误说明IIS服务器无法解析ASP代码
			if hasattr(e,'code') and 500<=e.code<600:  # if errors are 5xx, we try to open the page again
				return download(url,user_agent,number_retries-1)
	return html

def get_url(link):
	request=urllib.request.Request(link)
	html=urllib.request.urlopen(request).read().decode('gb2312')
	print(html)
	print(type(html))  # <class 'str'>

'''
	根据一个网址，正则匹配其中的网络资源。并下载
'''
def craw_by_sitemap(url):
	# get Domain Msg
	domain=getDomain(url)
	print(domain)
	# firstly, download the sitemap
	sitemap=download(url)
	# extract the links
	re_expression = R'<a\s+href="[\w/-]*"'
	links=re.findall(re_expression,sitemap)
	if links:
		#download each link
		for link in links:
			nextLinks=re.findall(R'/[\w/-]*[0-9]+',link)
			for next in  nextLinks:
				website=R'http://'+domain+next # 构建网址地图中包含的资源网址
				html = download( website )
				print( html )
				
				
				
'''
	to get the domain name of a URL，use urllib.parse module
'''
def getDomain(url):
	result=urllib.parse.urlparse(url)
	domain=result.netloc
	print(domain)
	return  domain


def crawling_by_id():
	# maximum number of consecutive download errors allowed
	max_errors=5
	#current number of consecutive download errors
	num_errors=0
	
	for page in itertools.count(1):   # to generate a series of numbers
		url='http://example.webscraping.com/view/-%d' %page
		html=download(url)
		if html is None:              # stop condition
			num_errors+=1     # received an errors when trying download this page
			if num_errors==max_errors:   # reach to the top of consecutive download errors allowed
				break
			
		else:
			num_errors=0    # download all pages successfully
def link_crawler(seed_url,link_regex):
	# craw following links which match with regex from the seed url
	crawl_queue=[seed_url]
	while crawl_queue:
		url=crawl_queue.pop()
		html=download(url)
		# filter for links matching our regular expressions
		for link in get_links(html):
			if re.match(link_regex,link):   # if re.match(link_regex,link) is not empty,which means matching successfully
				link=urllib.parse.urljoin(seed_url,link)  # to join 'http://example.webscraping.com' and the relative directory
				crawl_queue.append(link)

'''
re_expression = R'<a\s+href="[\w/-]*"'
	links=re.findall(re_expression,sitemap)
	if links:
		#download each link
		for link in links:
			nextLinks=re.findall(R'/[\w/-]*[0-9]+',link)
			for next in  nextLinks:
				website=R'http://'+domain+next # 构建网址地图中包含的资源网址
				html = download( website )
				print( html )
'''
def get_links(html):
	# return a list of links from html page
	# below define a regular expression for extracting all links from the page
	regex=re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
	# to list out all the links found in webpage
	re_expression = R'<a\s+href="[\w/-]*"'
	links = re.findall( re_expression, sitemap )
	if links :
		# download each link
		for link in links :
			nextLinks = re.findall( R'/[\w/-]*[0-9]+', link )
			for next in nextLinks :
				website = R'http://' + domain + next  # 构建网址地图中包含的资源网址
	
	return regex.findall(html)

if __name__ == '__main__':
	#g=download('http://www.meetup.com')
	#print(g)
	print('------------------')
	print('----------------------')
	#h=get_url('http://www.aihami.com/a/dangjian/shibada/256107.html')
	#h1=craw_by_sitemap('http://example.webscraping.com/sitemap.xml')
	re_expression =R'<a\s+href="[\w/]*"><img'
	sitemap="AAAAAAAAAA<a    href=\"sdlfjdlfj/ldfjflkdjfj\"><imgBBBBBBBBBBB\n1111111" \
	        "<a    href=\"sdlfjdlfjldfjflkdjfj\"><img555555555"
	links = re.findall( re_expression, sitemap )
	print(links[0])
	print('ABC'.encode('ascii'))
	print(len("中文")) # 计算中文字符数
	print(len("中文".encode("utf-8"))) # 计算字节数组长度
	h2=link_crawler('http://example.webscraping.com','/(index|view)')
	