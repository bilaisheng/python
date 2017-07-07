list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表\

print("\n********************************\n")

#列表中的元素是可以改变的
a = [1, 2, 3, 4, 5, 6];
a[0] = 9
print(a[0]);
a[2:5] = [13,14,15]
print(a)

a[2:5] = [] #删除
print(a)


a = list.copy()
print(a)
print(list.count(786))


print(a.reverse())