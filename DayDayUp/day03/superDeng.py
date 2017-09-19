# python的内置函数
#   绝对值函数abs（） 只能传入一个参数
abs(100)
abs(-100)
abs(12.34)
# 若传入参数不对 会报错typeError
# abs(1,2)
#   max （）函数 可以传入多个值，返回最大得那个
max(1,2,3,-5)

#  数据类型转换
#int（）函数，把其他数据类型转化为整数。
int('123') # 123
int(12.34) # 12
#float 函数
float('12.34')

#str()函数
str(100) # '100'
#bool函数
bool(1) # True
bool('') # False

# hex()函数 把一个整数转换为16进制表示的字符串

# 函数其实就是指向一个函数的引用，完全可以把函数赋给一个变量，相当于给这个函数起了一个别名
a=abs
a(-1) # 1

#  定义函数    使用def语句
def my_abs(x):
    if x >= 0:
         return x
    else:
          return  -x

#    计算x的平方的函数

def power(x):
    return  x*x

#  x的n次方
#       位置参数 调用参数时 ，传入值按照顺序依次赋值给x n
def power3(x,n):
    s = 1
    while n > 0:
        n = n-1
        s = s * x
    return s
print(power3(6,3))

#  例子：注册函数
def sin_up(name,gender):
    print('name',name)
    print('gender',gender)

 #    默认参数 默认参数可以简化函数的调用
    # 需要注意的：必选参数在前，默认参数在后，否则python解释器报错
    # 当函数有多个参数时，把变化大的参数放在前面，变化小的放后面，这样可以降低调用函数的难度。
def power4(x,n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s * x
    return s
#  当我们计算求x 的平方时就可以直接调用power4（）方法，例如 power（5),相当于调用了power（5,2）
power4(5)  # 25
power4(5,2)  #25
#  若需要传入不是2的数直接可以传入
power4(7,8)


# 默认参数需要注意的：
def add_end(L=[]):
    L.append('end')
    return L
#  正常调用
add_end([1,2,3]) # [1,2,3,'end']
# 如下调用就会出错 原因是默认参数[]，但是函数似乎每次都记住了上次调用。其实函数定义时，默认参数
# L的值就计算出来了，即[],因为默认参数L也是一个变量，每次调用时就会改变L的值。
# 所以定义默认参数的时候一定要指向不变对象。
add_end()  # ['end']
add_end()  #['end','end']

# 正确写法
def add_end(L=None):
    if L is None:
        L = []
    L.append('end')
    return  L

#       可变参数 就是传入的参数个数是可变的。
def calc(numbers):
    sum = 0
    for n in numbers:
        sum=sum+n*n
    return sum
# 调用时，需要组装一个list或tuple
calc([1,2,3])
calc((1,2,3))
# 简化写法 如果是可变参数

# 把函数的参数改为可变参数
def calc(*numbers):
     sum = 0
     for n in numbers:
         sum = sum + n * n
     return sum
calc(1,2,3)
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到是一个tuple，因此函数代码完全不变。但是，
# 调用改函数时，可以传入任意哥参数，包括0个参数。
calc(1,2) # 5
calc() #0l
#对于已经用一个list或者tuple
nums = [1,2,3]
calc(nums[0],nums[1],nums[2]) #14
#简化写法  可变参数就可如下写
nums = [1,2,3,4]
calc(*nums) #14

#    关键字参数 可变参数允许传入0个或任意哥参数，这些可变参数在调用时自动组装为一个tuple。
#   而关键字参数允许你传入0个或任意个参数名的参数，这些关键字参数在函数内部自动组装为你一个dict。
def person(name ,age , **kw):
    print('name:',name,'age:',age,'other:',kw)
    return ('name:',name,'age:',age,'other:',kw)
person('bilaisheng',30) #name:bilaisheng age: 30 other:{}
# 也可以传入任意个数的关键字参数
person('mike',32,city='shanghai')
person('admin',32,gender='M',job='engineer')
# 关键字函数的作用，可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和agez这两个参数，但是，如果调用者愿意提供更多的参数，我们也能接收到
eatra = {'city':'beijing','job':'engineer'}
person('jack',24,city=eatra['job']) #name:jack age:24 other:{'job':engineer}
# 简化写法
eatra = {'city':'beijing','job':'engineer'}
person('jack',56,**eatra)
# **extra表示吧extra这个dict的所有key-vaule用关键字参数传入到函数**kw参数，kw将获取一个dict，获得你dict是一份eatra的一份拷贝，对kw
# 看完的改动不会影响到函数外的ratra。

#    命名关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person(name, age, *, city, job):
    print(name, age, city, job)

person('super',25,city='beijing',job='engineer') #jack 25 beijing engineer

# 如果函数定义已经有了一个可变参数，后面跟着命名关键字参数就不再需要*
def student(name,age,*args,city,job):
 print(name,age,args,city,job)
# 命名关键字必须传入参数名，若传入参数名，调用将报错。

def student(name,age,*,city='beijing',job):
 print(name,age,city,job)
# 由于命名关键字参数可以有缺省值，调用时可以不传入city参数。
student('jack',25,job='study')

# 参数组合 可以用必选参数，默认参数，可变参数，关键字参数和命名关键字参数组合使用，参数定义的顺序：
# 必选参数，默认参数，可变参数，命名关键字参数和关键字参数。
def f1(a,b,c=0,*args,**kw):
 print('a=',a,'b=',b,'args=',args,'kw=',kw)

def f2(a, b, c=0,*,d,**kw):
 print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# * 可变参数，**关键字参数 区别调用*的时候将赋值转化为列表，调用**时转化为字典，特别注意的是* ，**可为空值。

# 普通函数和匿名函数。
# 普
def add(a,b):
    return a+b
print( add(2,3))
#  匿名函数的命名规则，用lamdba 关键字标识，冒号（：）左侧表示函数接收的参数（a,b） ,冒号（：）右侧表示函数的返回值（a+b）。
add = lambda a,b : a + b
print( add(2,4))

# Map 函數：計算字符串長度
abc = ['com','on','baby']
for i in range(len(abc)):
    print(len(abc[i]))
def length(nums):
    for i in nums:
     print(len(i))
length(['123','1','48974'])
abc_len = map(length,['com','on','baby'])


for i in abc_len:
    print(i)


# 通過map 函數轉化大小寫
def to_lower(item):
    return item.lower()
name = map(to_lower,['coOOh','rGfs','SSs'])

for i in name:
    print(i)

# map 函数加上匿名函数 求平方
squares = map(lambda x:x*x,range(9))
print (squares)

for i in squares:
    print(i)





