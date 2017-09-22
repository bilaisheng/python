#  用戶定义类，数字常量和内置数学工具和扩展，表达式操作符 递归阶乘
# 1.类的定义


# class Hotel(object):
#     # 构造函数
#     def __init__(self,room,cf=2.0,br=12):
#         self.room = room
#         self.cf = cf
#         self.br = br
#
#     def cal_all(self,days = 10):
#         return(self.room * self.cf + self.br)* days
# if __name__ == '__main__':
#     myroom = Hotel(100)
#     b_room = Hotel(200,0.8)
#     print(myroom.cal_all())
#     print(myroom.cal_all(2))
#     print(b_room.cal_all())
#     print(b_room.cal_all(2))
#
#
# # 2.父类，子类定义，以及子类调用父类
# # 父类
# class Fruit(object):
#     def __init__(self, color, shape):
#         self.color = color
#         self.shape = shape
#
#     def get_shape(self):
#         return self.shape
#
#
# # 子类继承
# class EmplFeel(Fruit):
#
#     def __int__(self,co, sh, feel):
#         # AddBook.__init__(selef, nm, ph) # 调用父类方法一s
#         super(EmplFeel, self).__init__(co, sh)
#         self.feel = feel
#
#     def get_feel(self):
#         return self.feel
#
# # 调用
# if __name__ == '__main__':
#
#     a = Fruit('red', 'circle')
#     b = Fruit('black', 'circle')
#     print(a.get_shape())
#     print(Fruit.get_shape(b))
#
#     c = EmplFeel('yellow', 'long', 'sweet')
#
#     print(c.get_feel(), c.get_shape())
#
# # 3.类的组合使用
# '''
# 1.class类的组合使用
# 2.手机、邮箱、QQ等是可以变化的（定义在一起），姓名不可变（单独定义）。
# 3.在另一个类中引用
# '''
#
#
# class Info(object):
#     def __init__(self,phone,email,qq):
#         self.phone = phone
#         self.email = email
#         self.qq = qq
#
#     def get_phone(self):
#         return self.phone
#
#     def update_phone(self,newphone):
#         self.phone = newphone
#         print("手机号更改已更改")
#
#     def get_email(self):
#         return self.email
#
#
# class Notebook(object):
#     def __init__(self,name,phone,email,qq):
#         self.name = name
#         self.info = Info(phone,email,qq)
#
# if __name__ == "__main__":
#     cj = Notebook('changjie', '397877802', '184548690@qq.com', '256413125')
#     print(cj.info.get_phone())
#     cj.info.update_phone(738423647)
#     print(cj.info.get_phone())
#     print(cj.info.get_email())

'''
**	x**y	x的y次方
//	x // y	两数相除向下取整
'''
x = 4
y = 3
print(x + y)  # 结果为 7
print(x - y)  # 结果为1
print(x * y)  # 结果为12
print(x / y)  # 结果为1.3333333333333333
print(x // y)  # 向下去整结果为1
print(x % y)  # 两数相除取余结果为1
print(x ** y)  # 4的3次幂结果为64

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

# 随机输出 1, 2, 3, 5, 9间的数
print("choice([1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9]))
# 输出 100 <= number < 1000 间的偶数
print("randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2))
# 生成第一个随机数
print("random() : ", random.random())
# 生成同一个随机数
random.seed(10)
print("Random number with seed 10 : ", random.random())
list = [8, 16, 10, 15];
random.shuffle(list)
print("随机排序列表 : ",  list)
print("uniform(3, 10) 的随机数为 : ",  random.uniform(3, 10))