# class Solution:
#     def twoSum(self, nums, target):
#         dict = {}
#         for i in range(len(nums)):
#             x = nums[i]
#             if target-x in dict:
#             dict[x] = i
# test = Solution
# print(test.twoSum([2, 7, 11, 15], 9))
#
#
# def twoSum(nums, target):
#     lis = []
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if target - nums[i] == nums[j]:
#                 lis.append(i)
#                 lis.append(j)
#     return lis
# print(twoSum([2, 7, 11, 15], 9))


import math
'''
使用math模块:(常用的一些函数)
sin(x)：求x的正弦                      cos(x)：求x的余弦                  asin(x)：求x的反正弦
acos(x)：求x的反余弦                   tan(x)：求x的正切                  atan(x)：求x的反正切
hypot(x,y)：求直角三角形的斜边长度      fmod(x,y)：求x/y的余数             ceil(x)：取不小于x的最小整数
floor(x)：求不大于x的正大整数           fabs(x)：求绝对值                  exp(x)：求e的x次幂
pow(x,y)：求x的y次幂                    log10(x)：求x的以10位底的对数      sqrt(x)：求x的平方根
'''
#  得到圆周率 pi
print(math.pi)

#  用help()查看每个函数的使用方法,如查看pow()方法，他会告诉你这是算n次方的
help(math.pow)

#  dir(module)是一个非常有用的指令，可以通过它查看任何模块中所包含的工具。
#  从上面的列表中就可以看出，在 math 模块中，可以计算正 sin(a),cos(a),sqrt(a)......
print(dir(math))

#  计算一个数的开方
print(math.sqrt(16))

#  四舍五入  round(需要操作的数据，保留小数位后几位)
print(round(1.1419,3))

'''
在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量
我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。
类似__xxx__这样的变量是特殊变量，可以被直接引用
类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用

'''

#  传入函数
#  既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x, y, f):
    return f(x) + f(y)
print(add(-5,6,abs))

#  上面的函数相当于
def add1(x,y):
    return abs(x)+abs(y)

'''
python 的函数
    1、构造函数统一命名__init__()，该方法是可选的，如果不提供，Python 会给出默认的__init__方法
    2、析构函数__del__()，当使用del 删除对象时，会调用他本身的析构函数，另外当对象在某个作用域中调用完毕，
       在跳出其作用域的同时析构函数也会被调用一次，这样可以用来释放内存空间。
    3、Python 采用垃圾回收机制来清理不再使用的对象；Python 提供gc模块释放
       不再使用的对象，Python 采用‘引用计数’ 的算法方式来处理回收，
       即：当某个对象在其作用域内不再被其他对象引用的时候，Python 就自动清除对象；
       Python 的函数collect()可以一次性收集所有待处理的对象(gc.collect())
'''
#  构造函数
#  “__init__”这个构造函数，具有初始化的作用，也就是当该类被实例化的时候就会执行该函数
class test(object):
    def __init__(self):
        print('我是构造函数，我在调用类的时候会对类进行初始化')
    def __del__(self):
        print('在删除对象的时候会调用')
tes = test()   # 在初始化的时候就开始执行__init__
del(tes)   # 当使用del 删除对象时，会调用他本身的析构函数

'''
类的定义：
    1、在python语言中，不管什么类型的实例都被看做对象，如整数也被作为对象看待，它属于int类
    备注：类的变量：由一个类的所有对象（实例）共享使用，只有一个类变量的拷贝，所以当某个
    对象对类的变量做了改动的时候，这个改动会反映到所有其他的实例上。我理解为：其实它就是
    一个类的全局变量，类实例化后的对象都可以调用该变量
    2、类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称，但是
       在调用这个方法的时候你不为这个参数赋值，Python会提供这个值。这个特别的变量指对象本身，按照惯例它的名称是self
域的定义：
    属于一个对象或类的变量被称为域，其实就是类里面定义的变量
    备注：由类的每个对象/实例拥有。因此每个对象有自己对这个域
    的一份拷贝，即它们不是共享的，在同一个类的不同实例中，虽然
    对象的变量有相同的名称，但是是互不相关的。我理解的是：不同的对象调用该变量，其值改变后互不影响
'''
class MyClass:
    count = 0
    name = 'czy'
    def __init__(self, name):
        self.name = name
        print('类的变量是： ',MyClass.name,'\n','对象的变量： ',self.name)
tess = MyClass('John')

'''
模块：
    1、如果你想要在其他程序中重用很多函数--------定义模块。其实就是很多的类型，很多的方法集合在一个或多个文件中，通过import ** 载入，类似于c#中的dll
       模块基本上就是一个包含了所有你定义的函数和变量的文件。为了在其他程序中重用模块，模块的文件名必须以.py为扩展名。
       注意：每个模块都有自己的名称__name__,__name__作为模块的内置属性，它的作用就是检测.py文件的调用方式，然后根据__name__做出相应的处理。
    2、模块有两种调用方式：1：被import载入调用  2：直接使用
    3、如果模块直接执行，__name__="__main__";  通常，此语句用于模块测试中使用。
'''
class ModuleClass:
    count = 0
    def __init__(self, name):
        self.name = name
        if(__name__ == "__main__"):
            print('这是这个类自己的模块')
        else:
            print('这个模块是其他地方的')
    def GetInfo(self):
        print(self.name)
#  测试
m = ModuleClass("Init")
m.GetInfo()

#  通过其他模块调用上面定义的  在其他模块执行
# import czyTestDemo4   导入模块
# s = czyTestDemo4.ModuleClass('其他模块')
# s.GetInfo()









