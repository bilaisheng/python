#!/usr/bin/python3
# Filename : feibonashulie.py
# Author by : Lily

def recur_fibo(n):
    """递归函数
    输出斐波那契数列"""
    if n <= 1:
        return n
    else:return (recur_fibo(n-1)) + recur_fibo(n-2)

# 获取用户输入
nterms = int(input("您要输出几项？"))
if nterms <= 0:
    print("请输入正数")
else:
    print("斐波那契数列：")
    for i in range(nterms):
        print(recur_fibo(i))
