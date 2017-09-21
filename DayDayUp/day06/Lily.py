"""
Day6:
迭代器与生成器
输入和输出
File(文件) 方法
OS 文件/目录方法
"""
from collections import Iterable
from collections import Iterator
import math
"""
可迭代对象
    直接作用于for循环的对象统称为可迭代对象：Iterable
    可以直接作用于for 循环的数据类型有：
    一类是集合数据类型：list,tuple,dict,set,str等
    一类是generator,包括生成器和带yield的generator function
    可以用isinstance()判断一个对象是否是Iterable
"""

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance((), Iterable))
print(isinstance(set(), Iterable))
print(isinstance('abcde', Iterable))
print(isinstance(135, Iterable))

"""
迭代器：
所有的Iterable均可以通过内置函数iter()来转变为Iterator。
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
对迭代器来讲，有一个__next()就够了。
在你使用for 和 in 语句时，程序就会自动调用即将被处理的对象的迭代器对象，
然后使用它的next__()方法，直到监测到一个StopIteration异常。

"""
print((x for x in range(10)), Iterator)
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance((), Iterator))
print(isinstance(set(), Iterator))
print(isinstance('abcde', Iterator))
L = [1,2,4,6]
I = iter(L)
print(next(I))
print(next(I))
print(next(I))
print(next(I))

"""
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。
在Python中，这种一边循环一边计算的机制，称为生成器：generator。
要创建一个generator，有很多种方法。
第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
"""
L = [x * x for x in range(10)]
g = (x * x for x in range(10))
print(type(L))
print(type(g))
print(next(g))
print(next(g))
for n in g:
    print(n)

"""
如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
"""
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5
o = odd()

print(next(o))
print(next(o))
print(next(o))

"""
Python两种输出值的方式: 表达式语句和 print() 函数。
第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout ?引用。
如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
str()： 函数返回一个用户易读的表达形式。
repr()： 产生一个解释器易读的表达形式。
"""

s = 'Hello,python!'
s1 = 124/9
print(str(s))
print(repr(s))
print(str(s1))
print(repr(s1))
print(repr('Hello,word\nPython')) #  repr() 函数可以转义字符串中的特殊字符
print(str('Hello,word\nPython'))

# rjust() 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。
# 如果指定的长度小于字符串的长度则返回原字符串。
# 还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。
# 另一个方法 zfill(), 它会在数字的左边填充 0
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
     # 注意前一行 'end' 的使用
    print(repr(x*x*x).rjust(4))


for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print('3423'.zfill(6))
print('abc'.ljust(8))
print('abc'.center(10))

# str.format() 的基本使用如下:
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
print('{0} 和 {1}'.format('Google', 'Runoob'))
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob',other='Taobao'))

# '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr())
# 可以用于在格式化某个值之前对其进行转化:
print('常量 PI 的值近似为： {!r}。'.format(math.pi))
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))

# 在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))

# 如果你有一个很长的格式化字符串, 而你不想将它们分开,
#  那么在格式化时通过变量名而非位置会是很好的事情。
# 最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值 :
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))

# % 操作符也可以实现字符串格式化。
# 它将左边的参数作为类似 sprintf() 式的格式化字符串,
# 而将右边的代入, 然后返回格式化后的字符串. 例如:
print('常量 PI 的值近似为：%5.3f。' % math.pi)

#  input() 置函数从标准输入读入一行文本，默认的标准输入是键盘。
#  input 可以接收一个Python表达式作为输入，并将运算结果返回。

# str = input("请输入：");
# print ("你输入的内容是: ", str)

"""
1.	file.close()
关闭文件。关闭后文件不能再进行读写操作。
5.	file.next()
返回文件下一行。
6.	file.read([size])
从文件读取指定的字节数，如果未给定或为负则读取所有。
7.	file.readline([size])
读取整行，包括 "\n" 字符。
8.	file.readlines([sizeint])
读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。
9.	file.seek(offset[, whence])
设置文件当前位置
10. 	file.tell()
返回文件当前位置。
11.	file.truncate([size])
从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后 V 后面的所有字符被删除，其中 Widnows 系统下的换行代表2个字符大小。
12.	file.write(str)
将字符串写入文件，没有返回值。
13.	file.writelines(sequence)
向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。

"""
# 打开文件
fo = open("knowledge", "r",encoding='utf-8')
print ("文件名为: ", fo.name)

line = fo.read(10)
print ("读取的字符串: %s" % (line))

# 关闭文件
fo.close()

# 打开文件
fo = open("knowledge", "r",encoding='utf-8')
print ("文件名为: ", fo.name)

for index in range(3):
    line = next(fo)
    print ("第 %d 行 - %s" % (index, line))

# 关闭文件
fo.close()

"""
1	os.access(path, mode)
检验权限模式
2	os.chdir(path)
改变当前工作目录
3	os.chflags(path, flags)
设置路径的标记为数字标记。
4	os.chmod(path, mode)
更改权限
5	os.chown(path, uid, gid)
更改文件所有者
6	os.chroot(path)
改变当前进程的根目录
7	os.close(fd)
关闭文件描述符 fd
"""
