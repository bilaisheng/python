# 文件读写
# StringIO和BytesIO
# 操作文件和目录
# 序列化

'''
f.read()
f.close()
f.readlines()
去掉每行最后的\n
line.strip()
读取图片 视频 rb 模式打开
结果为16进制表示的字节
'''

from io import StringIO
f = StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.write('world!'))
print(f.getvalue())

f = StringIO('Hello!\nHi\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

from io import BytesIO

f = BytesIO()
# 写入的不是str，而是经过UTF-8编码的bytes。
print(f.write('中文'.encode('utf-8')))
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())

# 操作文件和目录

import os

# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.name)
# 此处获取信息信息 ,但不再支持windows.
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
pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
'''
import pickle

# d = dict(name='Bob', age=20, score=88)
#
# print(pickle.dumps(d))
#
# f = open('dump.txt', 'wb')
# pickle.dump(d, f)
# f.close()

# f = open('dump.txt', 'rb')
# d = pickle.load(f)
# f.close()
# print(d)

# python对象转为json
import json

d = dict(name='Bob', age=20, score=88)
# dumps()方法返回一个str，内容就是标准的JSON。
print(json.dumps(d))

# JSON反序列化为Python对象，用loads()或者对应的load()方法，
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


# 此处分开,不可写到同一类下 ,
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Bob', 20, 88)
# print(json.dumps(s))

print(json.dumps(s, default=student2dict))

# 把任意class的实例变为dict
print(json.dumps(s, default=lambda obj: obj.__dict__))