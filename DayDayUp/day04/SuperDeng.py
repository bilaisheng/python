#   用戶定义类，数字常量和内置数学工具和扩展，表达式操作符递归阶乘
#  用户定义类
# class Worker(object):
#     def __init__(self, name, pay):
#      self.name = name
#      self.pay = pay
#     def lastName(self):
#         return self.name.split()[-1]
#
#     def giveRaise(self,percent):
#         self.pay *=(1.0+percent)
#
# if __name__ == '__main__':
#     bob = Worker('Bob smith', 50000)
#     sue = Worker('Sue jones', 60000)
#     bob.lastName()
#     print(bob.lastName())

# class Hotel(object):
#     # 构造函数
#     def __init__(self, room, cf=1.0, br=15):
#         self.room = room;
#         self.cf = cf;
#         self.br = br;
#
#     def calc_all(self, days=1):
#         return (self.room * self.cf + self.br) * days
#
# if __name__ == '__main__':
#     stdroom = Hotel(200)
#     big_room = Hotel(230, 0.9)
#     print(stdroom.calc_all())
#     print(stdroom.calc_all(2))
#     print(big_room.calc_all())
#     print(big_room.calc_all(2))

#  __init__ 方法的第一個参数永远是self，表示创建实例本身
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score=score
#     def print_score(self):
#         print('%s:%s' % (self.name, self.score))
#
#     def get_grade(self):
#          if self.score >= 90:
#              return 'A'
#          elif self.score >= 60:
#              return  'B'
#          else:
#              return 'C'
#
# if __name__ == '__main__':
#     bart = Student('xiaoliu', 98)
#     bart.print_score()

#  访问权限
# 如果不要内部属性被外部访问，可以把属性的名称加上两个下划线，实例变量如果以__开始，就变成了一个私有变量
# 只能内部访问外部访问不能
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

# 如果外部需要修改可以给类增加getset方法

# 继承多态
# 父类
class Animal(object):
    def run(self):
        print('Animal is running...')

# 子类
class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

# type判断类型

type(123) == type(456)  # True
type(123) == int  # True
type('abc')==type('123') # False

# 判断 对象是否为一个函数
# type(fn) == types.FunctionType
# type(abs)==types.BuiltinFunctionType
# type(lambda x: x)==types.LambdaType
# type((x for x in range(10)))==types.GeneratorType

# 判断继承关系 isinstance
# isinstance(h, Dog)

# 使用dir
dir('ABC')  # 可以获取到使用str对象的方法

#__XXX__属性和方法在python中有特殊用途
# 如果你调用len（）函数试图获取一个对象的长度时实际上在冷函数的内部会自动调用该对象___len__()
len('Abc')
'ABC'.__len__()

class MyDog(object):
    def __len__(self):
        return 100
# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
hasattr(obj, 'x')  # True 有属性‘x’吗
hasattr(obj, 'x')  # False 有属性‘y’吗
setattr(obj, 'y')  # 设置属性'y'
getattr(obj, 'y')  # h获取属性'y'

# 阶乘递归
def fact(n):
    if n == 1:
        return 1
    return  n * fact(n-1)
print(fact(5))

# Python数学函数
# 需要导入math 模块包
#  函数           返回值 ( 描述 )
# abs(x)     返回数字的绝对值，如abs(-10) 返回 10
# ceil(x)    返回数字的上入整数，如math.ceil(4.1) 返回 5
# cmp(x, y)  如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
# exp(x)     返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
# fabs(x)    返回数字的绝对值，如math.fabs(-10) 返回10.0
# floor(x)   返回数字的下舍整数，如math.floor(4.9)返回 4
# log(x)     如math.log(math.e)返回1.0,math.log(100,10)返回2.0
# log10(x)   返回以10为基数的x的对数，如math.log10(100)返回 2.0
# max(x1, x2,...)  返回给定参数的最大值，参数可以为序列。
# min(x1, x2,...)  返回给定参数的最小值，参数可以为序列。
# modf(x)    返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
# pow(x, y)  x**y 运算后的值。
# round(x [,n])   返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
# sqrt(x)    返回数字x的平方根，数字可以为负数，返回类型为实数，如math.sqrt(4)返回 2+0j
#
# 可以直接访问的数学函数：
# abs(x)     返回数字的绝对值，如abs(-10) 返回 10
# cmp(x, y)  如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
# max(x1, x2,...)  返回给定参数的最大值，参数可以为序列。
# min(x1, x2,...)  返回给定参数的最小值，参数可以为序列。
# round(x [,n])   返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
#
# Python随机数函数：
# python的随机数函数是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。
# 函数  描述
# choice(seq)    从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
# randrange ([start,] stop [,step])   从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
# random()       随机生成下一个实数，它在[0,1)范围内。
# seed([x])      改变随机数生成器的种子seed。
# shuffle(lst)   将序列的所有元素随机排序
# uniform(x, y)  随机生成下一个实数，它在[x,y]范围内。

# leeCode题目
def tow(nums, target):
 l2 = []
 len1=len(nums)
 for i in range(0,len1) :
    for j in range(i+1,len1):
           if(l[i]+l[j] == target):
               print(i)
               print(j)
               l2.append(i)
               l2.append(j)
 return l2


l = [3, 4, 5]
tow(l,9)





