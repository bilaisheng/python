# __str__
class student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

print(student('Michael'))

'''
这是因为直接显示变量调用的不是__str__()，而是__repr__()，
两者的区别是__str__()返回用户看到的字符串，而__repr__()
返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()
代码都是一样的，所以，有个偷懒的写法
'''
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__

# __iter__
'''
如果一个类想被用于for ... in循环，
类似list或tuple那样，就必须实现一个__iter__()方法，
该方法返回一个迭代对象，然后，Python的for循环就会不断调用
该迭代对象的__next__()方法拿到循环的下一个值，直到遇到
StopIteration错误时退出循环
'''


# 写一个斐波那契数列
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

# 测试
for n in Fib():
    print(n)

# __getitem__
# 上面的例子无法像list那样通过下标来取相应的值（Fib()[5]）,如果要想list那样取值的话需要
# 实现__getitem__ 方法


class fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f = fib()
print(f[5])

# 用__getitem__ 实现list切片的方法


class Fibs(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片,做输入类型的限制
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

s = Fibs()   # 测试
print(s[0:5])

# 补充
# 如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素

# __getattr__
# 为了避免调用类的方法或者属性时不存在而报错


class Students(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        if attr == 'age':
            return lambda: 25
# 测试调用类中没有定义的score属性和age函数
a = Students()
print(a.score)   # 能够正常返回
print(a.age)


