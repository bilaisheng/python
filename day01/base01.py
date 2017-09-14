#####输出格式化的字符串
print('Hi, %s, you have $%d.' % ('Michael', 1000000));
####变量
a=2;
b=a;
a=3;
print(b);
print(a);
print('''hang1
  ...hang2
  ...hang3''')
print ("hello world");
######输入语句
name=input();
print(name);
#input 输入的是str类型的
brith=input('brith:');
#int()函数 把数字类型的字符串变成数字类型。
birth_year=int(brith);

######r声明后面是非转义
print(r'\\\t\\')
print('\\\t\\')
#######b字节。两者显示一样但是内存不一样，bytes的每个字符只占一个字节
x1=b'ABC'
x2='ABC'
#####str通过encode()方法可以编码为指定的bytes--ascii、utf-8
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'));
#len()计算长度，可以是str，byte
print(len('ABC'));
print(len(b'ABC'));
print(len('中文'.encode('utf-8')));

#####list 索引是从0开始的。也可以从-1开始 用[]表示
classmates=['boy','gril','dog','11'];
print(len(classmates));
print(classmates[0]);
print(classmates[-1]);
#list的操作。list是可变的，可追加到末尾
classmates.append('amin');
#插入指定位置
classmates.insert(2,'serry');
#删除末尾
classmates.pop();
#删除指定位置
classmates.pop(1);
#要替换，直接赋值给对应的索引
classmates[1]='apple';
#list里面的类型可以不同
l=['a',1,True,['123','321']]
#######元组tuple  一旦初始化就不能修改的有序列表--安全，不变只的是指针位置不变，用（）表示
c=('123','54','665');
d=(1,) #只有一个元素也要加“，”
#可变的元组
t=('a','b',['A','b'])
t[2][0]='X';
t[2][1]='Y';
print(t);
####对字符串的操作。
a='123456';
#取值
print('--------'+a[1]);

print(a+'=======');
# 输出第一个到倒数第二个的所有字符
print(a[0:-1])
# 输出字符串第一个字符
print(a[0])
# 输出从第三个开始的后的所有字符
print(a[2:])
# 输出字符串两次
print(a * 2)
# 连接字符串
print(a + "TEST")
L = list("Python")
print(L)


l=list(a);
print(l);
# 用append（）方法，把新元素追加到list的末尾；insert（）可以将一个新元素添加到特定的位置。
l
# 删除元素
# 删除元素可以采用pop（）方法，执行L.pop()删除list的最后一个元素，
# 如果是特定位置的话可以采用pop（2），2表示的是位置。
############字典类似map 用{}表示
# 创建字典
y1 = {}
y1[1] = 2
print(y1)

M = {}
M['love'] = 'service'
print(M)

# 查找字典
#通过d[key]的方式,本质是根据dict查找
print(d['cat'])

# 遍历
d['dog'] = 'Ben'
for key in d:
    print(key + ":", d[key])
######判断
#if
big=6;
if big>=6:
    print('your number is'+big);
#if esle
big2=9;
if big2>1:
    print(big2);
else:
    print('small');
#elif 表示else if
age1=9;
if age1>18:
    print("adult");
elif age1>=6:
    print('teenger');
else:
    print('baby');

#if x:   只要x是非0数值，非空字符串，非空list，就判断为true。否则false。
x3=0;
if x3:
    print('True');
#########循环 可依次把元组tuple，list元素迭代出来。
#for  in
names=['superdeng','yisao','bilaoye','changjie','lily'];
for name in names:
    print(name);
sum=0;
for x4 in [1,2,3,4,5]:
    sum=sum+x4;
    print(sum);
###ranger函数  range（101）可以生成0-100的整数。
sum2=0;
for x5 in range(101):
    sum2=sum2+x5;
    print(sum2);
# while 循环
sum3=0;
n=9;
while n>0:
    sum3=sum3+n;
    print(sum3);


#####dict python内置字典 使用key-value。字典{}表示.一个key对应多个value时会把之前的value冲掉。
##dist特点：查找和插入的速度极快，不会随着key的增加而变慢；
#需要占用大量的内存，内存浪费多。
#而list相反：
#list特点
#查找和插入的时间随着元素的增加而增加；
#占用空间小，浪费内存很少。
#第一种初始化方式
d1={'cry':1,'smile':2}
print(d('cry'))
#第二种初始化方式
d1['kk']=67;
#第一种取值方式
print(d1['kk']);
#若key不在会报错，可以用in判断：
'cry' in d1
#第二种取值方式
d1.get('cry');

##########set，一组key的集合，不存储value，且key不能重复。
s1=set([1,2,3]);
print(s1);
#c重复的值会自动过滤
s2=set([1,1,2,2,3]);
#通过add方法添加到set（）方法里。
s1.add(4);#可重复加，但是不改变集合值。
#通过remove（）删除元素
s1.remove(4);
#两个set可以做数学意义上的交集、并集等操作：
s1&s2;
s1|s2;
#set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。

#########不可变对象内部是可以变化的
a=['3','2','1']
a.sort();

a2='abc';
a2.replace('a','A');


