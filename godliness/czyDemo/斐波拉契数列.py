#打印 max 个 斐波拉契数列
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b ,a + b
        n = n + 1

print(fib(10))

# 把fib 函数变成generator，可以用到yield
# def fib1(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield(b)
#         a, b = b, a + b
#         n = n + 1
# print(fib1(6))

#通过循环输出generator
# for n in fib1(6):
#     print(n)

