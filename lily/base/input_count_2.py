#!/usr/bin/python3
import string
content = ""
while True:
    s = input("请输入内容：")
    if s == "quit":
        break
    else:
        content += s
print("你输入的内容：%s" %content)

num , alpha , ch_alpha , blank , other = 0, 0, 0, 0, 0

for character in content in range(len(content)):
    # 判断该字符是否是数字，若是，num加1
    if character.isdigit():
        num += 1
    # 判断该字符是否是英文字符，若是，alpha加1
    elif character in string.ascii_letters:
        alpha += 1
    # 判断该字符是否是中文，若是，ch_alpha加1
    elif character.isalpha():
        ch_alpha += 1
    # 判断该字符是否是中文，若是，kong加1
    elif character == " ":
        blank += 1
    elif character == "quit":
        break
    # 判断若是其他字符，other加1
    else:
        other += 1

# 输出结果
print("你输入的内容包含数字{0}个，字母{1}个，汉字{2}个，空格{3}个，其他字符{4}个".format(num, alpha, ch_alpha, blank, other))





