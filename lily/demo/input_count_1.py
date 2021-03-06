#!/usr/bin/python3
# Filename: input_count_1.py
# Author by: Lily

# 判断输入的字符串中有几个数字，字母，汉字和空格
# 用到知识点：while;for;if...elif...else;.isdigit();.isalpha();.isspace();
import string
while True:
    # 初始化5个变量
    num, alpha, ch_alpha, blank, other = 0, 0, 0, 0, 0
    # 接收输入的内容
    s = input("请输入需要统计的内容:\n")
    # 遍历每一个字符
    for character in s:
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
        elif character.isspace():
            blank += 1
        elif character == "quit":
            break
        # 判断若是其他字符，other加1
        else:
            other += 1

# 输出结果
print("你输入的内容包含数字{0}个，字母{1}个，汉字{2}个，空格{3}个，其他字符{4}个".format(num, alpha, ch_alpha, blank, other))
