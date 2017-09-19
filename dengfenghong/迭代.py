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