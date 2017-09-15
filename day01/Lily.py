# python 有6中基本数据类型
# Number(数字) ，String(字符串), List(列表)，Tuple(元组),Dict(字典),Set(集合)

# 创建一个Number(数字)类型
a = 1
b = 2.3
c = 3 + 4j
d = True

# 同时创建多个数字类型
e, f, g = 1, 3.2, 3+3j

# 数字类型常用的运算符
sum = 4 + 6
sub = 6 - 2
mul = 5 * 1
divi = 8 /2
divi_1 = 9 // 2
mo = 19 % 5
print('sum =', sum, 'sub =', sub, 'mul =', mul, 'divi =', divi, 'divi_1 =', divi_1, 'mo =', mo)

# 创建一个String(字符串)类型
Name = 'My name is Lily'
Hobby = "reading, hiking, badminton"
introduce = '''
My name is Lily.
I'm 18 years old.
I like sports.
'''
print(Name)
print(Hobby)
print(introduce)

# 字符截取 拼接,叠加
print(Name[0])  # 截取Name的第一个字符
print(Name[-1])  # 截取Name的最后一个字符
print(Name+Hobby)   # 字符串拼接
print(Name*3)       # 字符串叠加

# 创建一个List(列表)类型
list = ['My', 'Name', 'is', 'Lily']
list1 = ['I', 'am', 18]
list3 = [134, 'python', [1, 3, 5]]

# List截取 拼接,替换
print(list[0])    # 按照索引取第一个元素
print(list[1:3])  # 切片取索引为1-2的元素
print(list+list3)   # 合并list和list3
print(list*2)     # list 叠加
list[0] = 'Your'    # 改变list[0]的值
print(list)
list.sort()           # 同类型的元素可以进行排序
print(list)
list.append('what!')   # 在列表末端添加元素
print(list)
list.pop()            # 删除最后一个元素，并返回该元素
print(list)

# 创建一个Tuple(元组)类型
tuple = (1, 2, 3, 'a', 'b', 'c')
tuple2 = ()
tuple3 = (333,)
print(tuple[0])         # 索引取值
print(len(tuple))       # 返回tuple的长度

# 创建一个Dict(字典)类型
student = {'name':'zhangshan','age':18,'weight':64}
print(student['name'])      # 获取字典中的和那么对应的值
student['name'] = 'lisi'    # 更新字典
print(student)
print(student.keys())       # 获取字典子所有的键
print(student.values())     # 获取字典中所有的值
del student['name']        # 删除'name':'zhangshan'这个键值对
student.clear()             # 删除student中的所有条目
print(student)

# 创建一个Set(集合)类型
s = set('pythonpython')
s.add('hello')          # 添加元素
print(s)
s.update('hello')       # 更新集合中的元素
print(s)
s -= set('pypi')         # 减掉集合中的元素
print(s)
s.remove('t')           # 移除集合中的元素
print(s)

# for 循环
keyword = ['a', 'b', 'c']
keyword2 = []
for k in keyword:
    print(k)

# for else 循环
for k in keyword:
    print(k)
else:
    print('No Data!')

# while 循环
i = 0
while i < 10:
    print(i)
    i += 1

# while else
j = 3
while j > 3:
    print(j)
else:
    print('j不大于3')


