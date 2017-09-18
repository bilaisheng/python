from random import randint

'''
    该方法传入两个参数
    lst：当前待排序列表
    reserve 若不传值，默认为True
    reserve = True 从大到小排列
    reserve = False 从小到大排列
'''
def bubbleSort(lst, reverse=True):
    # 获取列表长度
    length = len(lst)
    for i in range(0, length):
        for j in range(0, length - i - 1):
            # 比较相邻两个元素大小，并根据需要进行交换
            # 默认升序排序
            exp = 'lst[j] > lst[j+1]'
            # 如果reverse=True则降序排序
            if reverse:
                exp = 'lst[j] < lst[j+1]'
            if eval(exp):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


# 声明20个长度的list列表
lst = [randint(1, 100) for i in range(20)]

# 输出未排序前列表
print('Before sort:\n', lst)

# 开始排序
bubbleSort(lst, True)

# 输出排序后列表
print('After sort:\n', lst)
