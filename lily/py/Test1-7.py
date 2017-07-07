import csv
import codecs
import json
import urllib.request  #调用urllib2
url='http://crvweixin.crv.com.cn/activities/bind/cusBindPage!changeCity.action?imNumber=gh_de42836a07d5&t=Wed%20May%2018%202016%2011:21:11%20GMT+0800%20(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B76)&cid=7' #把等号右边的网址赋值给url
html=urllib.request.urlopen(url).read()   #html随意取名 等号后面的动作是打开源代码页面，并阅读
#print (html) #打印

n=0
s =  set([])
f =codecs.open('ki3.csv','w','utf_8_sig')
for j in json.loads(html):
	for k,v in j.items():
		f.write(k +',')
	break

f.write('\n')

for j in json.loads(html):
	for k,v in j.items():
		f.write(v.encode().decode('utf-8') +',')
	f.write('\n')

f.close()
