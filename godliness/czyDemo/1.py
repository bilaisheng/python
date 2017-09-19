#用列表代替循环生成1到10的平方数
a = [x * x for x in range(1,11)]
print(a)

#用列表模拟循环并且加上if筛选出仅偶数的平方
b = [x * x for x in range(1,11)if x%2==0]
print(b)

#使用两层循环生成全排列
c = [m + n for m in 'ABC' for n in 'XYZ']
print(c)

#把一个list中所有的字符串变成小写
#lower()方法把字符串变小写
L = ['Hello','World','IBM','Apple']
d = [s.lower() for s in L]
print(d)

#创建一个generator
e = (x * x for x in range(10))
print(e)




