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
