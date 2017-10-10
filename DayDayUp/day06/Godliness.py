# 迭代器与生成器
# 输入和输出
# File(文件) 方法
# OS 文件/目录方法

'''
    迭代器是访问集合元素的一种方式
    迭代器是一个可以记住遍历的位置的对象
    迭代器对象从集合的第一个元素开始访问 , 直到所有的元素被访问完结束.迭代器只能往前不会后退
    迭代器有两个基本的方法: iter() 和 next().
    字符串和列表或元祖对象都可用于创建迭代器.
'''

list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
print(next(it))  # 输出迭代器的下一个元素  :1
print(next(it))  # 输出迭代器的下一个元素  :2

# 使用常规for语句进行遍历
forlist = [1, 2, 3, 4]
forit = iter(forlist)  # 创建迭代器对象
for x in forit:
    print(x)

# 使用next函数

import sys

nlist = [1, 2, 3, 4]
nit = iter(nlist)

# while True:
#     try:
#         print(next(nit))
#     except StopIteration:
#         sys.exit()

'''
生成器
在python中,使用了yield 的的函数被称为生成器(generator)
跟普通函数不同的是,生成器是一个返回迭代器的函数,只能用于迭代操作,
更简单的理解生成器就是一个迭代器.
在调用生成器运行的过程中,每次遇到yield时函数会暂停并保存当前所有的运行信息.
返回yield的值.并在下一次执行next()方法时从当前位置继续运行
'''


def fibonacci(n):  # 生成器函数 - 斐波那契数列
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10)  # f是一个迭代器,由生成器返回生成

# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()


# 输入和输出

# x = input("请输入x = ")
# y = input("请输入y = ")
# z = x + y
# print("x+y=" + z)  # 此处返回为字符串拼接.如需要返回int 需用int()转换

# x = int(input("请输入x = "))
# y = int(input("请输入y = "))
# z = x + y
# print("x+y=", z)

# 格式化输出
# 第一种方式：自己控制
'''
字符串对象的 str.rjust() 方法的作用是将字符串靠右，并默认在左边填充空格，
所占长度由参数指定，类似的方法还有 str.ljust() 和 str.center() 。
这些方法并不会写任何东西，它们仅仅返回新的字符串，
如果输入很长，它们并不会截断字符串。 
'''
for x in range(1, 11):
    print(str(x).rjust(2), str(x*x).rjust(3), end=' ')
    print(str(x*x*x).rjust(4))

# 第二种是使用str.format()方法。
# 用法：它通过{}和:来代替传统%方式

# 1. 使用位置参数
li = ['hoho', 18]
print('my name is {} ,age {}'.format('hoho', 18))
print('my name is {1} ,age {0}'.format(10, 'hoho'))
print('my name is {1} ,age {0} {1}'.format(10, 'hoho'))
print('my name is {} ,age {}'.format(*li))

# 2. 使用关键字参数
# 要点：关键字参数值要对得上，可用字典当关键字参数传入值，字典前加**即可
hash = {'name': 'hoho', 'age': 18}
print('my name is {name},age is {age}'.format(name='hoho', age=19))
print( 'my name is {name},age is {age}'.format(**hash))

# 3. 填充与格式化
# 格式：{0:[填充字符][对齐方式 <^>][宽度]}.format()
print('{0:*>10}'.format(20))  # 右对齐
print('{0:*<10}'.format(20))  # 左对齐
print('{0:*^10}'.format(20))  # 居中对齐

# 精度与进制
print('{0:.2f}'.format(1/3))
print('{0:b}'.format(10))     # 二进制
print('{0:o}'.format(10))     # 八进制
print('{0:x}'.format(10))     # 16进制
print('{:,}'.format(12369132698))  # 千分位格式化

# 4. 使用索引
print(li)
print('name is {0[0]} age is {0[1]}'.format(li))


# Open a file
# fo = open("foo.txt", "wb")
# print("Name of the file: ", fo.name)
# print("Closed or not : ", fo.closed)
# print("Opening mode : ", fo.mode)
# fo.close()
# print("Closed or not : ", fo.closed)

print("===============")
# 打开一个文件
# f = open("foo.txt", "r", encoding= 'UTF-8')
# str = f.read()
# print(str)
# # 关闭打开的文件
# f.close()

# 打开一个文件
# f.readline() 会从文件中读取单独的一行。换行符为 ‘\n’。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
# f = open("foo.txt", "r", encoding='UTF-8')
# str = f.readline()
# print(str)
# # 关闭打开的文件
# f.close()

'''
f.readlines()
f.readlines() 将返回该文件中包含的所有行。 
如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。
'''

# 打开一个文件
# f = open("foo.txt", "r", encoding= 'UTF-8')
# str = f.readlines()
# print(str)
# # 关闭打开的文件
# f.close()
# # 另一种方式是迭代一个文件对象然后读取每行:
# # 打开一个文件
# f = open("foo.txt", "r", encoding="UTF-8")
# for line in f:
#     print(line, end='')
# # 关闭打开的文件
# f.close()
#
# '''
# f.write()
# f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。
# '''
# # 打开一个文件
# f = open("foo.txt", "w", encoding="UTF-8")
# num = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
# print(num)
# # 关闭打开的文件
# f.close()

# 如果要写入一些不是字符串的东西, 那么将需要先进行转换:
# 打开一个文件
f = open("foo.txt", "w",encoding="UTF-8")
value = ('www.baidu.com', 666)
s = str(value)
f.write(s)
# 关闭打开的文件
f.close()

# f.tell()
# f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。

'''
f.seek()
如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。 
from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如： 
seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符 
seek(x,1) ： 表示从当前位置往后移动x个字符 
seek(-x,2)：表示从文件的结尾往前移动x个字符 
'''
f = open('foo.txt', 'rb+')
f.write(b'0123456789abcdef')
print(f.seek(5))   # 移动到文件的第六个字节
print(f.read(1))
print(f.seek(-3, 2))  # 移动到文件的倒数第三字节
print(f.read(1))
f.close()