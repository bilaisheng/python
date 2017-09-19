import re
m1=re.match('/(.*)/(.*)/(.*)','/user/home/lumber')
l=m1.groups()
print(l)
m=re.match('hello[ \t]*(.*)world' ,'hello  super world')
l2=m.group(1)
print(l2)

# file
f = open('hello.txt','w')
f.write('hello\n')
f.write('world\n')
f.close()
t= open('hello.txt')
text=t.read()
t.close()
print(text)
st=text.split()
print(st)
detail=dir(f)
print(detail)
he=help(f.seek)
print(he)

# set 变成无序字典
x = set('spam')
y = {'h','a','m'}
print(x&y)
print(x|y)
print(x-y)
# list 转化为 set
t3 = {i ** 2 for i in[1,2,3,4]}
print(t3)
#  精确类型 decimal
import decimal
print(1/3)
d = decimal.Decimal(1/3)
print(d)
# 控制小数点位数
decimal.getcontext().prec = 2
d2 = decimal.Decimal('1.00') / decimal.Decimal('3.00')
print(d2)

# 分数
from  fractions import Fraction
f = Fraction(2,3)
print(f)
f1 = f + 1
print(f1)
# 函数type（）返回的是类型对象
print(type(l))
print(type(type(l)))

if type(l)== type(()):
    print('yes')
# 用的是类型名比较
if type(l) == list:
    print('yes')
if isinstance(l,list):
    print('yes')

