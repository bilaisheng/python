#忽略大小写按照字母表进行排序
def cmp_ignore_case(s1,s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return 1
    if u1 > u2:
        return -1
    return 0

def test1():
    a,b = 'B','A'
    flag = cmp_ignore_case(a,b)
    if flag > 0:
        return a+b
    if flag < 0:
        return b+a
    return '输入错误'
print(test1())
sorted(['D','A','C','B','F','G','E'],cmp_ignore_case)

