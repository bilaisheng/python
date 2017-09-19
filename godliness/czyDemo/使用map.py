#将一个函数作用在一个list上面
def f(x):
    return x * x
listA = range(10)
a = map(f,listA)

print(a)

