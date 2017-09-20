"""
Day 4:
用戶定义类，数字常量和内置数学工具和扩展，表达式操作符
递归阶乘
用列表生成式实现[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]。
函数实现斐波拉契数列
随机输入一串数字，用冒泡、选择、插入、快速法排序
"""

# 定义类
class Furniture(object):
    def __init__(self,name,price,count):
        self.name = name
        self.price = price
        self.count = count
    def print_price(self):
        print("%s%s"%(self.name,self.price))
    def get_total_price(self):
        return self.price * self.count

cost = Furniture('desk',300,2)
print(cost.get_total_price())

"""
数字常量：
pi  圆周率
e   自然常数

"""
"""
acos(x)	返回x的反余弦弧度值。
asin(x)	返回x的反正弦弧度值。	
atan(x)	返回x的反正切弧度值。
atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
cos(x)	返回x的弧度的余弦值。
hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)	返回的x弧度的正弦值。
tan(x)	返回x弧度的正切值。
degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)	将角度转换为弧度
"""

"""
1.算术运算符
+	加法运算，将运算符两边的操作数增加。	a + b = 31
-	减法运算，将运算符左边的操作数减去右边的操作数。	a – b = -11
*	乘法运算，将运算符两边的操作数相乘	a * b = 210
/	除法运算，用右操作数除左操作数	b / a = 2.1
%	模运算，用右操作数除数左操作数并返回余数	b % a = 1
**	对运算符进行指数(幂)计算	a ** b，表示10的21次幂
//	地板除 - 操作数的除法，其结果是删除小数点后的商数。 
    但如果其中一个操作数为负数，则结果将被保留，即从零(向负无穷大)舍去
    9//2 = 4 ， 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0
"""
print(2+4)
print(9-2)
print(5*3)
print(20/3)
print(40%3)
print(2**3)
print(42//5)

"""
2.比较(关系)运算符
==	如果两个操作数的值相等，则条件为真。	(a == b)求值结果为 false
!=	如果两个操作数的值不相等，则条件为真。	(a != b)求值结果为 true
>	如果左操作数的值大于右操作数的值，则条件成为真。	(a > b)求值结果为 false
<	如果左操作数的值小于右操作数的值，则条件成为真。	(a < b)求值结果为 true
>=	如果左操作数的值大于或等于右操作数的值，则条件成为真。	(a >= b)求值结果为 false
<=	如果左操作数的值小于或等于右操作数的值，则条件成为真。	(a <= b)求值结果为 true
"""
s = 8
if s ==18:
    print("你刚成年")
elif s < 18:
    print("你还未成年")
elif 40 >= s > 18:
    print("你还年轻")
else:
    print("你已经不在年轻")

"""
3.赋值运算符
=	将右侧操作数的值分配给左侧操作数	c = a + b表示将a + b的值分配给c
+=	将右操作数相加到左操作数，并将结果分配给左操作数	c + = a等价于c = c + a
-=	从左操作数中减去右操作数，并将结果分配给左操作数	c -= a 等价于 c = c - a
*=	将右操作数与左操作数相乘，并将结果分配给左操作数	c *= a 等价于 c = c * a
/=	将左操作数除以右操作数，并将结果分配给左操作数	c /= a 等价于 c = c / a
%=	将左操作数除以右操作数的模数，并将结果分配给左操作数	c %= a 等价于 c = c % a
**=	执行指数(幂)计算，并将值分配给左操作数	c **= a 等价于 c = c ** a
//=	运算符执行地板除运算，并将值分配给左操作数	c //= a 等价于 c = c // a
"""
a , b = 3, 5
a += 5
print(a)
b -= 3
print(b)
a *= 2
print(a)
b /= 3
print(b)
a %= 2
print(a)
b **= 3
print(b)
a //= 3
print(a)

"""
4.逻辑运算符
and	如果两个操作数都为真，则条件成立。	(a and b)的结果为False
or	如果两个操作数中的任何一个非零，则条件成为真。	(a or b)的结果为True
not	用于反转操作数的逻辑状态。	not(a and b) 的结果为True。
"""

# math库的内置方法：
"""
abs(x)          返回数字的绝对值
ceil(x)         返回数字的上入整数
cmp(x, y)	    如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1(pthon2有，python3没有)
exp(x)	        返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)	        返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)	    返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)	        如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)	    返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
modf(x)	        返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)	    x**y 运算后的值。
round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
sqrt(x)	        返回数字x的平方根
"""
import math
print(abs(-245))   # 输出245
print(math.ceil(3.2))    # 输出4
print(math.exp(4))       # 输出54.598150033144236
print(math.fabs(-20))    # 输出20.0
print(math.floor(2.6))   # 输出2
print(math.log(20))      # 输出2.995732273553991
print(math.log10(200))   # 输出2.3010299956639813
print(max(1,3,4))        # 输出4
print(min(1,4,2))        # 输出1
print(math.modf(2.58))   # 输出(0.5800000000000001, 2.0)
print(math.pow(2,3))     # 输出8
print(round(3.4553809,4))# 输出3.4554
print(math.sqrt(16))     # 输出4

"""
随机数函数
choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
random()	随机生成下一个实数，它在[0,1)范围内。
seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)	将序列的所有元素随机排序
uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。
"""
import random
print(random.choice([1,3,5,7,8]))
print(random.randrange(0,10))
print(random.random())
print(random.seed())
print(random.shuffle([1,5,7,2,4]))
print(random.uniform(3,7))

# 递归乘阶
def fact(n):
    if n==1:
        return n
    return n*fact(n-1)

print(fact(7))

# 用列表生成式实现[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]。
print([x * x for x in range(1,11)])


# 函数实现斐波拉契数列
# def recurfibo(n):
    # 递归函数 输出斐波那契数列
    # if n <= 1:
    #     return n
    # else:
    #     return (recurfibo(n-1)) + recurfibo(n-2)
# 获取用户输入
# nterms = int(input("您要输出几项？"))
# if nterms <= 0:
#     print("请输入正数")
# else:
#     print("斐波那契数列：")
#     for i in range(nterms):
#         print(recurfibo(i))

# 随机输入一串数字，用冒泡、选择、插入、快速法排序
# 1.选择排序
def selection(lista):
    leng=len(lista)
    for i in range(0,leng):
        index=i
        min=lista[i]
        for j in range(i,leng):
            if lista[j]<min:
                index=j
                min=lista[index]
        tmp=lista[i]
        lista[i]=lista[index]
        lista[index]=tmp
    return lista

# 2.插入排序
def insertion(lista):
    leng = len(lista)
    for i in range(1, leng):
        tmp = lista[i]
        j = i
        while (j > 0 and lista[j - 1] > tmp):
            lista[j] = lista[j - 1]
            j = j - 1
        lista[j] = tmp
    return lista

# 3.冒泡排序
def bubble(lista):
    leng=len(lista)
    for i in range(0,leng):
        for j in range(1,leng-i):
            if lista[j-1]>lista[j]:
                lista[j-1],lista[j]=lista[j],lista[j-1]
    return lista

print(bubble([3,76,8,3,9,4,2,9,5,33,21]))
print(insertion([3,76,8,3,9,4,2,9,5,33,21]))
print(selection([3,76,8,3,9,4,2,9,5,33,21]))