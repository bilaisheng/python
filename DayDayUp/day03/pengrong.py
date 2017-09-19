#!/usr/bin/env python3
# --*-- coding utf-8 --*--
#新建文件utf-8编码保存，Python3.5.2
# coding:utf-8
__author__='PengRong'

import  math
#函数调用实例
print(abs(-455.2));
print(int('127',base=8));

#函数定义实例
#无参数函数
def wucanshu():
    print("你好");
wucanshu();
#有参数函数
'''
定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None。

函数可以同时返回多个值，但其实就是一个tuple。
如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。

return None可以简写为return。
'''
def my_abs(x):
    '''
    自定义求绝对值的函数,其中isinstance(object, classinfo)
    的classinfo是tuple
    :param x:
    :return:
    '''
    #类型检查
    if isinstance(x,(str)):
        x=int(x);
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')

    if x>0:
        return  x;
    elif x<0:
        return -x;
print(my_abs(2));
print(my_abs('14523'));
#print(abs('A'));
'''
自定义一个空函数，pass语句是什么都不干的语句，
可以当做一个语句占位符，
有了pass就不会报语法错误
'''
def nop():
    pass;
#函数定义中包含一个默认参数
def move(x,y, step,angle=0):
    nx=x+step*math.cos(angle);
    ny=y+step*math.sin(angle);
    return nx,ny;
b=move(100,100,60,angle=math.pi/6);#b为tuple
print(b);

#递归调用
'''
使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出
'''
def fact(n):
    if n==1:
        return 1;
    return n*fact(n-1);

print('fact(10) '+str(fact(5)));

'''
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数
'''
#函数参数的一些用法
'''
#使用必须参数，默认参数、关键字参数,可变参数，使得函数定义出来的接口，不但能处理复杂的参数，
还可以简化调用者的代码
'''
#必须参数，函数调用必须赋值的参数
#默认参数，函数调用时可以也可以不赋值的参数
def power(x,n=2):
    '''
    一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；

    二是如何设置默认参数。
    默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，又可以传递更多的参数来实现
    :param x:  必须参数
    :param n: 有默认值的形参，默认参数
    :return:
    '''
    if not isinstance(x,(int,float)):
        raise  TypeError("传递参数类型有错");
    s=1;
    while n>0:
        n=n-1;
        s=s*x;
    return s;
print(power(2));
print(power(2,3));

#默认参数的坑
'''
原因解释如下：

Python函数在定义的时候，默认参数L的值就被计算出来了，默认参数L新建起来了
即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
'''
def add_end(L=[]):
    L.append('END')
    return L
print(add_end());
print(add_end());
#改进型号
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end());
print(add_end());

#可变参数，就是函数调用时候可以接受不定个数的形参，语法形式：*number
#定义一个接受可变参数的方法，方法参数前加*。
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
'''
参数numbers接收到的是一个tuple，但是，调用该函数时，可以传入任意个参数，包括0个参数：这些参数组装为tuple
'''
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + 2 * n
    return sum
print(calc(1.23,23,45));
print(calc(1,23,23,45));
'''
对于list 和tuple参数传递给可变参数只要如下,
务必对列表类型数据加*，不然整个列表当做一个元素传递给函数,比如
calc(nums)，函数获得的参数是（nums）只是含有一个元素的元祖
而calc(*nums)函数相当于将nums列表所有元素一个一个传递到函数，然后在函数里面组装为一个元祖，获得的参数是（1,2,3）使用
'''
nums=[1,2,3];
numsTuple=(4,5,6);
print(calc(*nums))
print(calc(*numsTuple));

def printVar(*string):
    print(string);

string=['java','math','engineer','network'];
printVar(*string);

#关键字参数允许你传入0个或任意个含参数名(参数名不限定)的参数，这些关键字参数在函数内部自动组装为一个dict
#体现在函数定义上就是形参名前多了两个**
def person(name,age,**kw):
    print('name: ',name,'age: ',age,'other: ',kw);
person('vincent',23);
person('vincent',23,city='guangzhou',code=57);
#或者这种形式,外部定义好了传递的数据包
extra ={'city':'guangzhou','code':57,'provice':'GD'};
person('cindy',56,**extra);

#命名关键字参数：限定了关键字参数的变量名,同时不能缺少这些限定关键字参数
#在关键字参数前需要一个 分隔符 *
'''

例如，只接收city和job作为命名关键字参数。这种方式定义的函数如下'''
def person(name, age, *, city, job):
    print(name, age, city, job)

#person('javk',24);#命名关键字参数不可缺少,调用函数时候必须用city='xxx',job='xxx'显示指定
person('javk',24,city='guangzhou',job='software')
extra={'city':"GZ",'job':'software'};
person('jack',26,**extra);

#具有可变参数和限定关键字参数函数
'''
如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
'''
def person(name,age,*args,city,job):
    print(name,age,args,city,job);

#由于调用时缺少参数名city和job，命名关键字参数不可缺少，Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数
#person('Jack', 24, 'Beijing', 'Engineer') #报错缺少后面两个命名关键字参数

person('Jack', 24, 'Beijing', 'Engineer',job='Engineer',city='GZ');


#命名关键字参数可以有缺省值，从而简化调用


def person(name,age,*args,city='GZ',job='Engineer'):
    print(name,age,args,city,job);

#使用了默认的命名关键字参数
person('Jack', 24, 'Beijing', 'Engineer');


'''
参数组合

在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、
命名关键字参数和关键字参数
'''
#必须参数，默认参数，可变参数，命名关键字参数，关键字参数
def CusPrint(name,age,gender='M',*args,city,job,**kws):
    '''

    :param name:
    :param age:
    :param gender: 默认参数
    :param args:
    :param city:
    :param job:
    :param kws:
    :return:
    '''
    print(name,age,gender,args,city,job,kws);

args1=(1,2,3);
args2={'gradle':2.5,'ant':3.7};
abc={'java':'1.8.5','python':'3.5.2'};
CusPrint('Vincent',20,'W',*args1,city='SZ',job='Engineer',**args2);

#必须参数，默认参数，可变参数，关键字参数
def CusPrint(name,age,gender='M',*args,**kws):
    print(name,age,gender,args,kws);
args1=(1,2,3);
CusPrint('Petty',56,'M',*args1,**abc);
CusPrint('Petty',56,*args1,**abc);

#必须参数，默认参数，可变参数，命名关键字参数
'''
按顺序匹配
如果可变长参数放在前面，则后面的默认参数，除非指定名称，否则无法匹配，只能使用默认值（无默认值，则会保存）。
如果可变长参数放在后面，则会先那一个参数给默认参数，剩下的属于可变长参数。
'''
#必须参数，默认参数，可变参数，命名关键字参数
def CusPrint(name, age, gender='M', *args, city):
    print(name, age, gender, args, city);
args1=(1,2,3);
CusPrint('Jantly',34,*args1,city='GanZhou');
CusPrint('Jantly',34,'W',*args1,city='GanZhou');

#必须参数，默认参数，可变参数，关键字参数
def CusPrint(name, age, gender='M', *args,**kws):
    print(name,age,gender,args,kws);
args1=[1,2,3];
keyValue={'C':'c89','C++':'C11'};
CusPrint('CP',24,'M',*args1,**keyValue);

#必须参数，默认参数，命名关键字参数，关键字参数
def CusPrint(name, age, gender='M', *, city,job, **kws):
    print(name, age, gender, job, city,kws);
CusPrint('Askty',78,'W',city='BeiJing',job='English',**args2);
CusPrint('Askty',78,city='BeiJing',job='English',**args2);