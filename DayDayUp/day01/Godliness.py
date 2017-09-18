# Python3 中有六个标准的数据类型
# 字符串(String)
# 数字(Digit)
# 列表(List)
# 元祖(Tuple)
# 集合(Sets)
# 字典(Dictionary)
# 日期(Date)

# 如果不想 \ 在字符中发生转义, 可以在字符串前面增加 r 或者 R ,表示原始字符串

print('转义前 : ' + 'C:\some\name')
print("转义后 : " + r'C:\some\name')
string = 'Runoob'
print(string)  # 输出字符串
print(string[0:-1])  # 输出第一个到倒数第二个的所有字符
print(string[0])  # 输出字符串第一个字符
print(string[2:5])  # 输出从第三个开始到第五个的字符
print(string[2:])  # 输出从第三个开始的后的所有字符
print(string * 2)  # 输出字符串两次
print(string + "TEST")  # 连接字符串


# 创建Tuple
# 与list不同的是，tuple采用（）括起来
T = 1, 2, 3
print(T)

T = (1, 2, 3)
print(T)

T = "abc"
print(T)
# 创建空元组：T = ()
# 定义一个元素的元组
# 这样运行了结果是对的，看起来也没错，但是这种定义其实并不正确，这种定义的不是tupel，
# 而是1这个数，这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，
# 因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
# 所以定义含一个元素的元组时必须加一个逗号，
T = (1)  # not correct
print(T)

T = (1,)  # correct

# 访问
T = (1, 2, 3)
print(T[1])
# 更改
# 定义的tuple是不变的，可以在tuple中定义list对其进行修改
T = (1, 2, ['a', 'b'])
print(T[2][0])
T[2][0] = 'c'
print(T)
# 在tuple中，虽然元素不可以修改，但是我们可以对其进行连接组合
T1 = [1, 2, 3]
T2 = [4, 5, 6]
T3 = T1 + T2
print(T3)

# 创建list
L1 = [1, 2, 3]
print(L1)

L2 = ['abc']
print(L2)

L3 = ["a", "b", "c"]
print(L3)

# 会对字符串进行单个字符拆分
L = list("Python")
print(L)

# 访问list
print(L[0])
print(L[-1])
# 添加新元素
# 用append（）方法，把新元素追加到list的末尾；insert（）可以将一个新元素添加到特定的位置。
# 删除元素
# 删除元素可以采用pop（）方法，执行L.pop()删除list的最后一个元素，
# 如果是特定位置的话可以采用pop（2），2表示的是位置。


# 创建字典
d1 = {}
d1[1] = 1
print(d1)

d = {}
d['cat'] = 'Lucy'
print(d)

# 查找字典
# dict是通过key来查找value，表示的是意义对应的关系，可以通过d[key]的方式
print(d['cat'])

# 遍历
d['dog'] = 'Ben'
for key in d:
    print(key + ":", d[key])
# dict的第一个特点是查找速度快，而且查找的速度与元素的个数无关，
# 而list的查找速度是随着元素的增加而逐渐下降的
# 第二个特点是存储的key-value序对是没有顺序的
# 第三个特点是作为key得到元素是不可变的，所以list不能作为key。
# dict的缺点是占用内存大，还会浪费很多内容。

# 创建Set
# dict是建立了一系列的映射关系，而set是建立一系列无序的，不重复的元素。
# 创建set的方式是调用set()并传入一个list，list的元素将作为set的元素。
S = set([1, 2, 3])
print(S)

# 自动过滤重复元素
S = set([1, 1, 2, 3, 4, 5, 4])
print(S)

# 添加
# add()添加，有重复元素可以添加，但不会有效果：
S.add(6)
S.add(7)
print(S)

# 删除
S.remove(6)
print(S)

# 交集，并集
S1 = set([1, 2])
S2 = set([2, 3])
print(S1 & S2)
print(S1 | S2)
# set和dict的唯一区别仅在于没有存储对应的value.set的原理和dict一样
# 同样不可以放入可变对象因为无法判断两个可变对象是否相等
# 无法保证set内部不会有重复元素


# list，tuple，dict和set的主要区别
'''
1.list
list是一个使用方括号括起来的有序元素集合;
List 可以作为以 0 下标开始的数组,任何一个非空 list 的第一个元素总是 L[0],负数索引从 list 的尾部开始向前计数来存取元素。任何一个非空的 list 最后一个元素总是 L[-1];
有分片功能，两个list可以相加；
append 向 list 的末尾追加单个元素；
insert 将单个元素插入到 list 中； 
extend 用来连接 list，使用一个 list 参数进行调用；
append 接受一个参数, 这个参数可以是任何数据类型, 并且简单地追加到 list 的尾部；
index 在 list 中查找一个值的首次出现并返回索引值； 
要测试一个值是否在 list 内, 使用 in, 如果值存在, 它返回 True, 否则返为 False ；
remove 从 list 中删除一个值的首次出现；
pop 可以删除 list 的最后一个元素, 然后返回删除元素的值，用索引删除制定位置的值；

2.tuple
tuple是不可变的list，创建了一个tuple就不能以任何方式改变它；
定义tuple是将整个元素集是用小括号括起来，是有序集合；
tuple的索引与list一样从0开始,所以一个非空的tuple的第一个元素总是t[0]；
负数索引与 list 一样从 tuple 的尾部开始计数；
与 list 一样分片 (slice) 也可以使用。分割一个 tuple 时, 会得到一个新的 tuple；
没有 append、extend、remove或pop方法以及index方法；
可以使用in来查看一个元素是否存在于tuple 中。

3.dict
dict定义了键和值之间的一一对应关系，每个元素都是一个key-value对；
整个元素集合用大括号括起来，有序集合；
可以通过 key 得到value, 但不能通过vaule获取 key；
在一个 dict中不能有重复的 key, 并且 key 是大小写敏感的；
键可以是数字、字符串或者是元组等不可变类型；
用del使用key可以删除dict中的独立元素； 
用clear可以清除dict中的所有元素。

4.set
set是建立一系列无序的，不重复的元素；
创建set的方式是调用set()并传入一个list，list的元素将作为set的元素；
set和dict的唯一区别仅在于没有存储对应的value。
'''
# 循环
sites = ["Baidu", "Google", "Runoob", "Taobao"]

for site in sites:
    if site == "Runoob":
        print("Runoob : "+site)
        break
    else:
        print("当前站点名称为" +site)
#
# count = 0
# while count < 5:
#    print(count, " 小于 5")
#    count = count + 1
# else:
#    print(count, " 大于或等于 5")