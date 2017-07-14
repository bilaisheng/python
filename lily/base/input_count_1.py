#!/usr/bin/python3

# 使用while循环使用该方法


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
        elif character.lower() or character.upper():
            # 'a'<character<'z' or 'A'<character<'Z':  #in string.ascii_letters:
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
