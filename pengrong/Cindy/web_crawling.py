#!/usr/bin/env python3
# --*-- coding utf-8 --*--
#新建文件utf-8编码，Python3.5.2
# coding:utf-8
__author__ = 'PengRong'

import urllib.request
import re
import  chardet
import urllib.parse

def download(url,user_agent='wsp',number_retries=2):
	print('downloading:'+url)
	headers={'user-agent':user_agent}
	request=urllib.request.Request(url,headers=headers)
	try:
		context = urllib.request.urlopen(request)
		print(context.getcode())
		headers=context.getheaders()
		#headers['Content']
		html=context.read()
		charset=chardet.detect(html)['encoding']
		print(charset)
		html=html.decode(charset)
		print(html)
		#decode( 'utf-8' )
		print(type(html))   #<class 'bytes'>,it is a bytes object without decode
	except urllib.request.URLError as e:
		print('download errors:',e.reason)
		html=None
		if number_retries>0:
			if hasattr(e,'code') and 500<=e.code<600:
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
def craw_sitemap(url):
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
	获取一个网址的域名，使用urlparse 模块
'''
def getDomain(url):
	result=urllib.parse.urlparse(url)
	domain=result.netloc
	print(domain)
	return  domain

if __name__ == '__main__':
	#g=download('http://www.meetup.com')
	#print(g)
	print('------------------')
	print('----------------------')
	#h=get_url('http://www.aihami.com/a/dangjian/shibada/256107.html')
	#h1=craw_sitemap('http://example.webscraping.com/sitemap.xml')
	re_expression =R'<a\s+href="[\w/]*"><img'
	sitemap="AAAAAAAAAA<a    href=\"sdlfjdlfj/ldfjflkdjfj\"><imgBBBBBBBBBBB\n1111111" \
	        "<a    href=\"sdlfjdlfjldfjflkdjfj\"><img555555555"
	links = re.findall( re_expression, sitemap )
	print(links[0])
	print('ABC'.encode('ascii'))
	print(len("中文")) # 计算中文字符数
	print(len("中文".encode("utf-8"))) # 计算字节数组长度
	