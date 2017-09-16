# import os
# import sys
# #获取当前所工作的目录的名称
# #得到D:\AllWorkSpace\python_space\python\DayDayUp\day02
# f = os.getcwd()
# print(f)
# #打印系统平台的名称
# print(sys.platform)
# #range(1,10)为1——9
# #打印九九乘法表
# print('第一种方法：')
# for i in range(1,10):
#     for a in range(1,i+1):
#         re = str(i*a)  #将相乘结果转换成str用于拼接
#         rs = str(i)+'*'+str(a)+'='+re
#         #end为结束后追加的内容
#         print(rs,end='\t')
#     print('\n')
#
# print('第二种方法：')
# for i in range(1, 10):
#     for j in range(1, i+1):
#         # %前为占位符 后面括号中参数对应占位符位置, end 结束后追加的内容
#         print("%d*%d=%d" % (i, j, i*j), end="\t")
#     print("")
#
# print('第三种方法：')
# i = 1
# while i < 10:
#     if i == 1:
#       j = i
#       print("%d*%d=%d" % (i, j, i * j), end="\t")
#       i = i + 1
#     else:
#         j = 1
#         while j < i+1:
#             print("%d*%d=%d" % (i, j, i * j), end="\t")
#             j = j + 1
#         i += 1
#     print("")
#
# # 列表(List)
# #定义一个空列表
# list=[]
#
# #想列表中添加数据 append()方法，默认在末尾追加，
# list.append('A')
# list.append('B')
# print(list)
#
# #若想在特定的位置插入数据可以用 insert（）
# list.insert(1,'C')
# print(list)
#
# #计算list中某个元素出现的次数
# list.count('A')
# print(list.count('A'))
#
# #向列表中添加一个列表 默认在末尾追加
# list.extend(['E','F','G'])
# print(list)
#
# #删除list中的元素 pop() 根据下标 默认删除最后一个 可以指定位置(如果打印的话可以得到具体删除的那个元素)
# list.pop()
# print(list)
# print(list.pop(4))
#
# #删除列表中具体的元素 remove
# list.remove('A')
# print(list)
#
# #获得元素在list中的位置
# print(list.index('B'))
#
# #颠倒列表的顺序
# list.reverse()
# print(list)
#
# #将list的成员重新排序
# list.sort()
# print(list[:2])


# 元祖(Tuple)
# 集合(Sets)
# 字典(Dictionary)
