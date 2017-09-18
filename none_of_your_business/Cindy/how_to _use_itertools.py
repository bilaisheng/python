#!/usr/bin/env python3
# --*-- coding utf-8 --*--
#新建文件utf-8编码保存，Python3.5.2
# coding:utf-8
__author__='PengRong'

import itertools

'''
this module is kind of similar to generator in python, we can not compare itertools.count(1) with a number,
only when we get the elements of it, we can use the element to compare with a number
'''
n=itertools.count(1,3)   # start, step
for i in n:
	#print(type(n))   # <class 'itertools.count'>
	#print(type(i))   # <class 'int'>
	if i <9999:       # to give A STOP CONDITION, if not, the program will run forever
		print(i)
	else:
		break
'''


# to create a cycle in which 'a','b','c','d','e'  will repeat again and again
g=itertools.cycle('abcde')   # <itertools.cycle object at 0x00000000033576C8>
                            
for i in g:
	print(type(i))    #<class 'str'>
	print(i)
'''


s=itertools.repeat('ABC',4)  # to repeat 'ABC' for 4 times
print(s)
for i in s:
	print(i)
