"""
Day6:
迭代器与生成器
输入和输出
File(文件) 方法
OS 文件/目录方法
"""
from collections import Iterable
from collections import Iterator
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
print((x for x in range(10)), Iterator)
"""
所有的Iterable均可以通过内置函数iter()来转变为Iterator。
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

"""
