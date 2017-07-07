
from math import sqrt

from pip._vendor.distlib.compat import raw_input

start = int(raw_input('请输入开始数字 ： '))
end = int(raw_input('请输入开始数字 ： '))
h = 0
leap = 1
for m in range(start+1,end+1):
    k = int(sqrt(m + 1))
    for i in range(2,k + 1):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        print ('%-4d' % m)
        h += 1
        if h % 10 == 0:
            print ('')
    leap = 1
print ('The total is %d' % h)