# Tuple（元组）
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号(())里，元素之间用逗号隔开。
# 元组中的元素类型也可以不相同


tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组.

tup = (1, 2, 3, 4, 5, 6)
print(tup[0])
print(tup[1:5])

#tup[0] = 11  # 修改元组元素的操作是非法的
#报错为：tuple' object does not support item assignment


tup1 = ()    # 空元组
tup2 = (20,) # ****一元素，需要在元素后添加逗号****


