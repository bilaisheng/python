# 1. 数据类型 (类型转换 .每个类型常用方法, )
#python的数据类型有1、字符串 2、布尔类型 3、整数 4、浮点数
# 5、 数字 6、列表 7、元组 8、字典 9、日期

#字符串---用单引号或双引号括起来
str = 'who are you ?'
str2 = 'i am String'
print(str+'  '+str2)
#还有一种三引号，在三引号中可以自由使用单引号或双引号
str3 = '''我说：“很高兴认识你”'''
print(str3)

#将字符串转换为一个整型
x = '1'
y = int(x)
print(y)
#整型转换为字符串
a = 1
b = '%d' %a
print(a)
#将字符串转换为一个浮点型
str4 = '4.1'
c = float(str4)
print(c)
#将浮点型转换为字符串
d = 4.1021
str5 = '%f'%d
print((str5))








# 2 字符操作(截取 拼接,替换 等)
# 3 循环(for ,  for else , while ,while else 常用循环判断)