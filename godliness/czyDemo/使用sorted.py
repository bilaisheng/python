#实现倒序排序
def reversed_cmp(x,y):
    if x>y:
        return -1
    if x<y:
        return 1
    return 0
a = sorted([36,5,25,6,9,78,40],reversed_cmp )
print(a)