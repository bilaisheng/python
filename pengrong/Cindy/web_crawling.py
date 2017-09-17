#!/usr/bin/env python3
# --*-- coding utf-8 --*--
#新建文件utf-8编码，Python3.5.2
# coding:utf-8
__author__ = 'PengRong'

import urllib.request
import re

def download(url,user_agent='wsp',number_retries=2):
	print('downloading:'+url)
	headers={'user-agent':user_agent}
	request=urllib.request.Request(url,headers=headers)
	try:
		html=urllib.request.urlopen(request).read().decode('utf-8')
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

def craw_sitemap(url):
	# firstly, download the sitemap
	sitemap=download(url)
	# extract the links
	re_expression='<loc>(.*?)</loc>'
	links=re.findall(re_expression,sitemap)
	#download each link
	for link in links:
		html=download(link)
		print(html)
	

if __name__ == '__main__':
	g=download('http://www.meetup.com')
	print(g)
	print('------------------')
	print('----------------------')
	h=get_url('http://www.aihami.com/a/dangjian/shibada/256107.html')
	h1=craw_sitemap('http://example.webscraping.com/sitemap.xml')
	