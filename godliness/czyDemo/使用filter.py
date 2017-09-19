#去掉一个list中的偶数只留下奇数
# def is_odd(n):
#     return n%2==1
#
# a = filter(is_odd,range(10))
# print(a)

#把一个序列中的空字符串去掉
def not_empty(s):
    return s and s.strip()
b = filter(not_empty,['A','','B','C','','D','','E','F'])
print(b)

