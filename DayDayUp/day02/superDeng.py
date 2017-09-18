# 1、字符串：序列操作、编写字符串的其他方法、模式匹配
S='abcd'
print(len(S))

S[0]   # 'a'
S[1]   # 'b'
S[-1]  # 'd'
S[1:2]  # bc
S[1:]  # bcd
S[:2]  # abc
S[:-1] # abc
S[:] # abcd
S +  'efg' #abcdefg
S * 3 # abcdefg abcdefg abcdefg

# 特定函数
# find函数 没有找到时返回-1
S.find('b') #  1
# replace（）
S.replace('a','XYZ')

# upper() 大写
S.upper()

# isalpha() 测试字符串的内容 ，True ，False
S.isalpha();
# S.rstrip();去空
S.rstrip();
# 帮助文档 help
help(S.replace)

#编写字符的其他方法
s = 'A\nb\tc'
len(s) # 5

ord('\n')  # 10
# r 表示后面的为非转义
print(r'//t//t//n')

# 模式匹配
# 搜索子字符串，这个子字符串以“hello”开始，后面跟着0空格或几个空格或制表符，接着有任意字符并将其保存到group中，最后以world结尾。
import re
match = re.match('hello[ \t]*(.*)world','hello   python world')
match.group(1) # 输出'python '

match = re.match('/(.*)/(.*)/(.*)','/user/home/lumjack')
match.groups()  #输出（'user','home','lumberjack'）


# 2、列表（列表的基本操作）

#序列操作
l = [123,'spam',1.22]
# 求列表长度
len(l)
# 第一个元素
l[0]
# 倒数第一个之前的元素
l[:-1]
# 把一个list 放入另一个 但是不能改变原list的

l+[1,2,3]
# 类型特定的操作 不能改变原list
# 删除对应位置的元素 list从0开始。
l.pop(2)
# 添加元素到末尾
l.append('4897')
# 任意位置插入元素
#l.insert(1，22)
# 任意位置移除元素
#l.remove(2)

# 排序
m = [9,5,7,4,6]
m.sort()
# 元素倒转
m.reverse()
# 嵌套
n = [[1,2,3],[4,5,6],[7,8,9]]
print(n[1])
print(n[1][2])
# 列表解析
col2=[row[1] for row in n]
# col2 [2,5,8] 实现矩阵操作
[row[1] + 1 for row in n]
[row[1] for row in n if row[1] % 2 == 0]

diag = [n [i][i] for i in [0,1,2]]
print('diag:'+[n [i][i] for i in [0,1,2]])
doubles = [c * 2 for c in 'spam']

# 利用sum函数 转化为元组 或者字典
g = (sum(row) for row in n)
next(g) #  6
next(g) # 15
 # 对各行的统计
list(map(sum,n))
print(list(map(sum,n))) # [6,15,24]
{sum(row) for row in n}
{i:sum(n[i]) for i in range(3)}
# 列表、集合和字典都可以解析创建

# 阶乘递归
def fact(n):
    if n == 1:
        return 1
    return  n * fact(n-1)
print(fact(5))

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

# 取一个list或tuple部分元素
L=['pengrong','super','bilaisheng','chenzhongyi','changjie','lily']
# 笨方法
[L[0],L[1]]
# 切片
L[0:2]
d = {'a':1,'b':2,'c':3}
for key in d:
    print(key)
for ch in 'ABC':
    print(ch)
from collections import Iterable
# 是否为可迭代对象 -整数，小数不能
isinstance('abc',Iterable)
# 下标循环
for i,value in enumerate(['A',"b","c"]):
    print(i,value)
for x,y in [(1,2),(2,3),(3,4)]:
    print(x,y)

# 1
l1=list(range(1,7))
print(l1)
l2=[]
for x in range(1,11):
    l2.append(x*x)
print(l2)
# 简化写法
l3 = [x*x  for x in range(1,11)]
print(l3)
# 全排列
l4 = [m + n for m in 'ABC' for n in 'abc']
print(l4)
# 导入os模块 下面的可以列出文件和目录
import  os
l5=[d for d in os.listdir('.')]
print(l5)

d = {'1':'a','2':'b','3':'c'}
for k, v in d.items():
    print(k,v)
# 列表生成式可以生成列表
l6 = [k + '=' + v for k,v in d.items()]
# 把list的元素变成小写
L = ['H','B','C']
l7 = [L.lower() for s in L]
print(l7)

import string

# while实现
n = 9
j = 0
i = 0
while i < n:
    i = i + 1
    while j < i:
        j = j + 1
        print("%d * %d =%d" % (j, i, i * j), end="\t")
        if(j==i):
            j=0
            break
    print(" ")

#  3、打印九九乘法口诀和循环输出26个字母(并将字母的Ascall码同时输出)
for i in string.ascii_lowercase:
    print(str( i ) +r'  '+ str(ord(i)))

for i in range(1,10):
    for j in range(1,i+1):
        print("%d * %d = %d" % (j,i,j*i),end="\t")
    print(" ")












