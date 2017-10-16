# 文件读写
# 讀文件
f = open('D:test.txt', 'r')
t = f.read()
print(t)
f.close()
# 讀文件可能會報錯IOError
try:
    f = open('D:test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# with 語句自動調用close方法
f = open('D:test.txt', 'r')
with open('D:test.txt', 'r') as f:
    print(f.read())
# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便
f = open('D:test.txt', 'r')
for line in f.readlines():
    print(line.strip())

# file-like Object
# 像open函數返回這種有個read方法的對象，在python中統稱為file-like，出來file
# 還可以是內存的字節流，網絡流，自定義流等，不要求特定類繼承，只要read方法就行

# 二進制文件
# f = open('D:test.jpg', 'rb')
# print(f.read())

# 字符編碼 open默認讀取的是utf-8編碼文件，若要指定讀取格式插入encoding,若轉碼有錯加error可忽略。
f = open('D:test.txt', 'r', encoding='gbk', errors='igore')
# 寫文件
f = open('D:test.txt', 'w')
f.write('world')
f.close()
# 同樣with可以省虐f.close

# StringIO和BytesIO
# 要把 str寫入StingIO
from  io import  StringIO
f = StringIO()
print(f.write('hi'))
# getvalue方法用於獲得寫入后的Str。
print(f.getvalue())

f2 = StringIO('Hello!\n Hi! \n Goodbye!')
while True:
    s = f2.readline()
    if s == '':
        break
    print(s.strip())

# BytesIO
# StringIO操作只能是Str  而二進制就要使用 BytesIO
from io import BytesIO
f3 = BytesIO()
f3.write('中午'.encode('utf-8'))
print(f3.getvalue())
f4 = BytesIO(b'\xe4\xb8\xad\xe5\x8d\x88')
print(f4.read())
# 操作文件和目录
import os
# print(os.name)
# print(os.uname)
# print(os.environ)
# print(os.environ.get('PATH'))
# 查看當前目錄的絕對路徑
print(os.path.abspath('.'))
# 在某個目錄下創建一個新目錄，首先把新目錄的完整路徑表示出來
print(os.path.join('/users/michael', 'testdir'))
# 創建一個目錄
# os.mkdir('/users/michael/testdir')
# 刪除目錄
# os.rmdir('/users/michael/ testdir')
# 把兩個路徑合成一個時，不要直接拼接字符串，而是要通過
# os.path.join()函數
# 同樣要拆分路徑時，通過os.path.split函數
# 這些合併拆分路徑的函數不要求目錄和文件真存在，他們只是對字符串操作

# python過濾文件
[x for x in os.listdir('.')
 if os.path.isfile(x)]
# 只列出特定文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

# 序列化
# 對象序列化并寫入文件
import pickle
d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))
# pickle.dumps()方法任意對象序列化成一個bytes。然後，就可以把bytes寫入文件
# 或者利用pickle.dump方法直接把對象序列化后寫入一個file-likeobject

f6 = open('d:dump.txt', 'wb')
pickle.dump(d, f6)
f6.close()
#  從磁盤督導內存 先把內容督導一個bytes，然後pickle.loads()方法飯序列化對象
f7 = open('d:dump.txt', 'rb')
d2 = pickle.load(f7)
f7.close()
print(d2)

import json
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))
# 把json反序列化
json_str='{"age":20, "score":88, "name":"bob"}'
print(json.loads(json_str))
# Json 進階


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student('Bob', 20, 88)
# 報錯
# print(json.dumps(s))


def student2dict(std):
    return {
        'name':std.name,
        'age': std.age,
        'score':std.score
    }
# student實例先被student2dict函數轉化為dict，然後在轉化為JSON
print(json.dumps(s, default=student2dict))