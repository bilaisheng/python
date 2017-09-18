# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

from pip._vendor.distlib.compat import raw_input

str = raw_input("请输入待统计字符串：")

letters = 0
space = 0
digit = 0
others = 0

for i in str:
    if i.isdigit():
        digit += 1
    elif i.isspace():
        space += 1
    elif i.isalpha():
        letters += 1
    else:
        others += 1

print ('char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others))
