#!/usr/bin/env python3
# --*-- coding utf-8 --*--
#新建文件utf-8编码保存，Python3.5.2
# coding:utf-8
__author__='PengRong'

import re
str='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa22222222222aaaaaaaaaaaaaaaaaaa111111111111111111111111111111111111111111bbb99999'
str11='012345'
str_list=['22222222222','333333','0123456789']

expression=re.compile('\d{10}')
print(expression.match(str))
g=re.match('\d{10}',str)
h=[]
h.append(g)
print(h)

#re.findall(pattern, string,flags)  it returns a list

print(re.findall('\d{10}',str))  # we can only give a string as argument, we can not give it a list
                    # in this example, we hope to grep 10 numbers from the string, if there isn't enough bits, no result
print(re.findall('\d{10}',str11))  # an empty list

# re.match(pattern, string, flags)
m=re.match('foo','foofootball') #<_sre.SRE_Match object; span=(0, 3),match successfully
n=re.match('foo','seafood')  # None, which means not match successfully
j=re.match('foo','barfood')  # None, which means not match successfully
print(m,n,j)
if m is not None:
	m.group()
	print(m.group())     # foo

# look above, when should know that m satisfy the regular expression conditions, through m.group, we will get the matched object:foo



# search mode, when there is 'foo' included in the string, it is matched
search=re.search('foo','seafoodfootball')
print('匹配对象search:',search)   #匹配对象search: <_sre.SRE_Match object; span=(3, 6), match='foo'>

bt='bat|bet|bit'  #pattern
bt1='bat'+'bet'+'bit'
bat=re.match(bt,'bat')  #<_sre.SRE_Match object; span=(0, 3), match='bat'>
bit=re.match(bt1,'is it bit?')  #None
bet=re.search(bt,'is it bet?')  #<_sre.SRE_Match object; span=(6, 9), match='bet'>
print(bat,bet,bit)

tmpstr='.end'
lala=re.match(tmpstr,'tend')   # <_sre.SRE_Match object; span=(0, 4), match='tend'>
print('lala:',lala)
wlwl=re.match(tmpstr,'hhend')  # None, more than one character before 'end'
print('wlwl:',wlwl)
blank=re.match(tmpstr,'\nend') # None, special characters not count
print('blank:',blank)
ff=re.search(tmpstr,'is end!')   # <_sre.SRE_Match object; span=(2, 6), match=' end'>
print('ff:',ff)


# if there is . in the pattern, we need to transform
pi='3\.14'
p=re.match(pi,'3.14')
print(p)


