# 文件读写
# StringIO和BytesIO
# 操作文件和目录
# 序列化
'''
读取文件内容，需要以读文件的模式打开一个文件对象，用Python的内置函数open（），传入文件名和标识符
读取文件分三步，
1、用open()函数打开，如若传入的文件地址不存在，会抛出IOError
2、调用read()方法一次读取文件的所有内容，Python会用一个str对象表示
3、读取完毕，用close()方法关闭文件（必须关闭）

f=open('notfound.txt','r')
f.read()
f.close()
'''
#引入with()语句，自动调用close()方法
#优点：不用每次打开一个文件，就要写一个close()

with open('path/tp/file','r') as f :
    print(f.read())
'''
因为read()每次是读取全部内容，如果文件较大，内存会爆满，可以使用read(size)方法，
size表示每次最多读取的字节数。
调用readline()，可以每次对一行内容,
readlines() 一次读取所有内容，饼按行返回list.
如果文件很小，read()一次性读取最方便,
如果不能确定文件大小，反复调用read(size)比较保险,
如果是配置文件，调用readlines()最方便
'''
for line in f.readlines():
    print(line.strip())  #末尾的‘\n’删掉

#读取二进制未见，比如图片、视频等，用‘rb’模式打开文件即可：
#f = open('/Users/michael/test.jpg', 'rb')

#要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
f = open('/Users/michael/gbk.txt', 'r', encoding='gbk',errors='ignore')  #直接忽略遇到的编码问题

#写入文件，即在open()打开一个文件对象时，以写入文件的模式打开，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
f = open('/Users/kiki/test.txt','w')
f.write('Hello,World!')
f.close()
#当我们写文件时，操作系统不会马上把数据写入磁盘，而只是在内存缓存起来，空闲时才写入。
#只有在调用close()方法时，操作系统才会保证把没有写入的数据全部写入磁盘。如果忘记调用close）
#数据可能只写了一部分，剩下没写入的就丢失了。所以还是采用with语句稳妥
with open('/Users/kiki/test.txt','w') as f:
    f.write('Hello,World!')
#写入特定编码的文本文件，要给open()函数传入一个encoding参数，将字符自动转换成指定编码

#在内存读写时，使用StringIO和BytesIO
#读写str时使用StringIO，读写二进制数据时，使用BytesIO
#写入时，需要创建一个StringIO或BytesIO，然后像文件一样写入即可：
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())
f = StringIO('Hello!\nHi\nGoodbye!')
while True:
    s = f.readline()
    if s==' ':
        break
    print(s.strip())
#输出结果>>>hello world!
#用getvalue() 获得写入后的str,也可以用readline()方法进行读取
from io import BytesIO
f = BytesIO()
# 写入的不是str，而是经过UTF-8编码的bytes
print(f.write(('中文'.encode('utf-8'))))
print(f.getvalue())
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())

# 操作文件和目录
import os
# 如果输出是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.name)
# 此处获取系统信息 ,但不再支持windows.
# print(os.uname())
# 查看操作系统中定义的环境变量
print(os.environ)
# 获取某个环境变量的值
# print(os.environ.get('PATH'))
# 查看当前目录的绝对路径
# print(os.path.abspath('.'))
# 在某个目录下创建一个新的目录,首先把新目录的完整路径表示出来
# print(os.path.join('d:/', 'testdir'))
# 创建一个目录
# os.mkdir('d:/testdir')
# 删除一个目录
# os.rmdir('d:/testdir')
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数
# print(os.path.split('d:/testdir/file.txt'))
# os.path.splitext()可以直接得到文件扩展名
# print(os.path.splitext('d:/testdir/file.txt'))
# 对文件重命名:
# os.rename('test.txt', 'test.py')
# 删掉文件:
# os.remove('test.py')
# 要列出当前目录下的所有目录
# print([x for x in os.listdir('.') if os.path.isdir(x)])
# 列出所有的.py文件
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
# 序列化
'''
pickle.dumps()方法把任意对象序列化成一个bytes,然后，就可以把这个bytes写入文件。
或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
'''
import pickle
#d = dict(name='Bob',age=20,score=88)
# print(pickle.dumps(d))
# f = open('dump.txt', 'wb')
# pickle.dump(d, f)
# f.close()
# f = open('dump.txt', 'rb')
# d = pickle.load(f)
# f.close()
# print(d)

# python对象转为json
import json
d = dict(name='Bob',age=20,score=88)
# dumps()方法返回一个str，内容就是标准的JSON
print(json.dump(d))
# Json反序列化为Python对象，用loads()或者对应的load()方法
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
}

s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))
# 把任意class的实例变为dict
print(json.dumps(s, default=lambda obj: obj.__dict__))


















