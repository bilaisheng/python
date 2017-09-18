# 题目：利用递归方法求任意输入的正整数阶乘。

from pip._vendor.distlib.compat import raw_input

#阶乘方法
def fact(j):
    total = 0
    if j == 0:
        total = 1
    else:
        total = j * fact(j - 1)
    return total

n = int(raw_input("请输入一个正整数："))

for i in range(1,n+1):

    # 此处输出当前输入整数之前包括本身在内的所有正整数的阶乘
    print ('%d! = %d' % (i,fact(i)))

    #此处仅输出输入正整数阶乘
    if i == n:
        print('%d! = %d' % (i, fact(i)))