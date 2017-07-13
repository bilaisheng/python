# !/usr/bin/python3
# Filename : Armstrong_number
# Author by : Lily

# Python 检测用户输入的数字是否为阿姆斯特朗数
while True:
    # 获取用户输入的数字
    num = int(input("请输入一个数字："))
    # 初始化sum
    sum = 0
    # 指数
    n = len(str(num))

    # 检测
    # 方法一：
    # temp = num
    # while temp > 0:
    #     digit = temp % 10
    #     sum += digit ** n
    #     temp //=10
    # 方法二：
    for i in str(num):
        sum += int(i)**n

    #输出
    if num == sum :
        print("%d 是阿姆斯特朗数" %num)
    else:
        print("%d 不是阿姆斯特朗数" %num)
