import sys  # 引入 sys 模块

# 迭代器与生成器
# 迭代器
list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
print(next(it))  # 输出迭代器的下一个元素
print(next(it))

'''
迭代是Python最强大的功能之一，是访问集合元素的一种方式。。
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。
字符串，列表或元组对象都可用于创建迭代器：
'''

# 迭代器对象可以使用常规for语句进行遍历
list = [1, 2, 3, 4]
it = iter(list)
for x in it:
    print(x, end=" ")

# #  也可以用next()函数
# list = [1, 2, 3, 4]
# it = iter(list)  # 创建迭代器对象
#
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

'''
使用了 yield 的函数被称为生成器（generator）

生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，
返回yield的值。并在下一次执行 next()方法时从当前位置继续运行。
'''


def gen():
    yield 5
    yield "Hello"
    yield "World"
    yield 4

for i in gen():
    print(i)
# 输入和输出
# Python两种输出值的方式: 表达式语句和 print() 函数。
# 第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
s = 'hello python'
print(str(s))
print(repr(s))  # 将输出的值转成字符串
x = 10 * 3.25
y = 200 * 200
s = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
print(s)
#  repr() 函数可以转义字符串中的特殊字符
hello = 'hello, runoob\n'
hellos = repr(hello)
print(hellos)

# 有两种方式输出一个平方与立方的表:
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')  # 字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格
    # 注意前一行 'end' 的使用
    print(repr(x * x * x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))  # 括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换

# input 可以接收一个Python表达式作为输入，并将运算结果返回
# str = input("请输入：")
# print("你输入的内容是：",str)

# 打开文件
# fo = open("123.txt", "wb")
# print("文件名为: ", fo.name)
#
# # 关闭文件
# fo.close()

'''	
file.close()  关闭文件。关闭后文件不能再进行读写操作
file.flush() 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入
file.fileno() 返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上
file.isatty() 如果文件连接到一个终端设备返回 True，否则返回 False。
file.next()   返回文件下一行。
file.read([size]) size未指定则返回整个文件,如果文件大小>2倍内存则有问题.f.read()读到文件尾时返回""(空字串)
file.readline() 返回一行
file.readline([size]) 返回包含size行的列表,size 未指定则返回全部行  读取整行，包括 "\n" 字符。
'''
# 打开文件
# fo = open("123.txt", "r")
# print("文件名为: ", fo.name)
#
# for index in range(5):
#     line = next(fo)
#     print("第 %d 行 - %s" % (index, line))
#
# # 关闭文件
# fo.close()

# 只读文件的前5行：
f = open("123.txt", "r", encoding='utf-8')
for i in range(5):
    print(f.readline())

# 以列表的方式读取这个文件
f = open('123.txt', 'r', encoding='utf-8')
for line in f.readlines():
    print(line)

fo = open("123.txt", "r")
#显示文件的编码
print(fo.encoding)
'''
w     以写方式打开，
a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
r+     以读写模式打开
w+     以读写模式打开 (参见 w )
a+     以读写模式打开 (参见 a )
rb     以二进制读模式打开
wb     以二进制写模式打开 (参见 w )
ab     以二进制追加模式打开 (参见 a )
rb+    以二进制读写模式打开 (参见 r+ )
wb+    以二进制读写模式打开 (参见 w+ )
ab+    以二进制读写模式打开 (参见 a+ )
'''

# OS 文件/目录方法
import os
print(os)
# 返回一个目录的绝对路径
print(os.path.abspath("python_modu"))

# 返回一个目录的基名
print(os.path.basename("/usr/local/python3/bin/python3"))

# 返回一个目录的目录名
print(os.path.dirname("/usr/local/python3/bin/python3"))

# 测试指定文件是否存在
print(os.path.exists("/usr/bin/python"))
print(os.path.exists("/home/egon"))

# # 得到指定文件最后一次的访问时间
# print(os.path.getatime("/root/changjie.py"))
'''
getctime 得到指定文件最后一次的改变时间
getmtime 得到指定文件最后一次的修改时间
getsize  得到文件的大小
isfile 测试指定参数是否是一个文件
'''