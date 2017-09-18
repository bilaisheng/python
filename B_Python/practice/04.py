
#键入任意整数，将之从小到大输出
from pip._vendor.distlib.compat import raw_input

#声明一个空元组
l = []

length = int(raw_input("请输入想要比较的长度 : "))

#range(1,3) -->1,2 不包含3
for i in range(1,length+1):
    x = int(raw_input("请输入比较的第"+str(i)+"个整数为："))
    #追加用户输入数值到元组中
    l.append(x)

#对l从小到大排序
l.sort()

#输出l
print(l)

######此处不可用下列写法输出######
#print(l.sort())    输出结果为None
