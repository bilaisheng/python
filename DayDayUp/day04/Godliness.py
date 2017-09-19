# 用戶定义类，数字常量和内置数学工具和扩展，表达式操作符递归阶乘

__author__ = 'bilaisheng'

'''
　1.类的定义
　2.父类，子类定义，以及子类调用父类
　3.类的组合使用
　4.内置功能
'''


# 类的定义


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

# 父类 子类以及调用父类

# 父类
class AddBook(object):
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def get_phone(self):
        return self.phone


# 子类继承
# class EmplEmail(AddBook):
#
#     def __int__(self,nm, ph, email):
#         # AddBook.__init__(selef, nm, ph) # 调用父类方法一
#         super(EmplEmail, self).__init__(nm, ph)
#         self.email = email
#
#     def get_email(self):
#         return self.email
#
# # 调用
# if __name__ == '__main__':
#
#     detian = AddBook('Detian', '12345678901')
#     meng = AddBook('Meng', '12345678902')
#     print(detian.get_phone())
#     print(AddBook.get_phone(meng))
#
#     alice = EmplEmail('godliness', '1234567890', 'godliness@qq.com')
#
#     print(alice.get_email(), alice.get_phone())

# 类的组合使用

'''
1.class类的组合使用
2.手机、邮箱、QQ等是可以变化的（定义在一起），姓名不可变（单独定义）。
3.在另一个类中引用
'''

# class Info(object):
#     def __init__(self, phone, email, qq):
#         self.phone = phone
#         self.email = email
#         self.qq = qq
#
#     def get_phone(self):
#         return self.phone
#
#     def update_phone(self, newphone):
#         self.phone = newphone
#         print("手机号更改已更改")
#
#     def get_email(self):
#         return self.email
#
#
# class AddrBook(object):
#     def __init__(self, name, phone, email, qq):
#         self.name = name
#         self.info = Info(phone, email, qq)
#
#
# if __name__ == "__main__":
#     Detian = AddrBook('godliness', '1234567890', '1234567890@qq.com', '123456')
#     print(Detian.info.get_phone())
#     Detian.info.update_phone(738423647)
#     print(Detian.info.get_phone())
#     print(Detian.info.get_email())

'''
**	x**y	x的y次方
//	x // y	两数相除向下取整
'''

x = 5
y = 3
a = 4
b = 2
print(x + y)  # 结果为 7
print(x - y)  # 结果为2
print(x * y)  # 结果为15
print(x / y)  # 结果为1.6666666666666667 不同的机器浮点数的结果可能不同
print(x // y)  # 向下去整结果为1
print(x % y)  # 两数相除取余结果为2
print(x ** y)  # 5的3次幂结果为125

print(a / b)  # 结果为浮点数2.0
print(a % b)  # 取余结果为0
print(a // b)  # 取整结果为2

'''
关系运算符是对两个对象进行比较。

运算符	表达式	        说明
==	    a==b	        等于，比较对象是否相等
!=或<>  a !=b ,a <>b    不等于，比较两个对象是否不相等
'''
a = 4
b = 2
c = 2
print(a == b)  # False
print(a != b)  # True
print(a > b)  # True
print(a < b)  # False
print(a >= b)  # True
print(c <= b)  # True

a = 4
b = 2
c = 0
print(a > b and b > c)  # a>b为True继续计算b>c，b>c也为True则结果为True
print(a > b and b < c)  # a>b为True继续计算c<b，b>c结果为False则结果为False
print(a > b or c < b)  # a>b为True则不继续计算c<b，结果为True
print(not c < b)  # c<b为True not True结果为False
print(not a < b)  # a<b为False not Flase结果为True

a = 4
c = 0
list = [1, 2, 3, 4, 5]
if (a in list):
    print("%d is in list:%r" % (a, list))
if (c not in list):
    print("%d is not in list: %r" % (c, list))


# Python数学函数：

'''
需要导入math 模块包
 函数           返回值 ( 描述 )
abs(x)     返回数字的绝对值，如abs(-10) 返回 10
ceil(x)    返回数字的上入整数，如math.ceil(4.1) 返回 5
cmp(x, y)  如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
exp(x)     返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)    返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)   返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)     如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)   返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)  返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)  返回给定参数的最小值，参数可以为序列。
modf(x)    返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)  x**y 运算后的值。
round(x [,n])   返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
sqrt(x)    返回数字x的平方根，数字可以为负数，返回类型为实数，如math.sqrt(4)返回 2+0j

可以直接访问的数学函数：
abs(x)     返回数字的绝对值，如abs(-10) 返回 10
cmp(x, y)  如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
max(x1, x2,...)  返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)  返回给定参数的最小值，参数可以为序列。
round(x [,n])   返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。

Python随机数函数：
python的随机数函数是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。
函数  描述
choice(seq)    从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])   从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
random()       随机生成下一个实数，它在[0,1)范围内。
seed([x])      改变随机数生成器的种子seed。
shuffle(lst)   将序列的所有元素随机排序
uniform(x, y)  随机生成下一个实数，它在[x,y]范围内。
'''

import random

print("choice([1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9]))
# 输出 100 <= number < 1000 间的偶数
print("randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2))
# 生成第一个随机数
print("random() : ", random.random())
# 生成同一个随机数
random.seed(10)
print("Random number with seed 10 : ", random.random())
list = [20, 16, 10, 5];
random.shuffle(list)
print("随机排序列表 : ",  list)
print("uniform(5, 10) 的随机数为 : ",  random.uniform(5, 10))

'''
Python三角函数：
Python三角函数是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。 
 函数            描述
acos(x)     返回x的反余弦弧度值。
asin(x)     返回x的反正弦弧度值。 
atan(x)     返回x的反正切弧度值。
atan2(y, x) 返回给定的 X 及 Y 坐标值的反正切值。
cos(x)      返回x的弧度的余弦值。
hypot(x, y) 返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)      返回的x弧度的正弦值。
tan(x)      返回x弧度的正切值。
degrees(x)  将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)  将角度转换为弧度
'''

import math

print("degrees(3) : ",  math.degrees(3))
print("radians(-3) : ",  math.radians(-3))
print("sin(3) : ",  math.sin(3))
print("cos(3) : ",  math.cos(3))
print("tan(3) : ",  math.tan(3))
print("acos(0.64) : ",  math.acos(0.64))
print("asin(0.64) : ",  math.asin(0.64))
print("atan(0.64) : ",  math.atan(0.64))
print("atan2(-0.50,-0.50) : ",  math.atan2(-0.50,-0.50))
print("hypot(0, 2) : ",  math.hypot(0, 2))

'''
Python数学常量：
常量              描述
 pi      数学常量 pi（圆周率，一般以π来表示）
 e       数学常量 e，e即自然常数（自然常数）。
'''
print(math.pi)
print(math.e)