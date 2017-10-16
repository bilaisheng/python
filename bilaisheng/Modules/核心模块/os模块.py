import os

# 返回一个目录的名称
print(os.path.basename("d:/python"))

# 返回一个目录的目录名
print(os.path.dirname("d:/python/bilaisheng"))

# 测试指定文件是否存在
print(os.path.exists("d:/python"))

# 得到指定文件最后一次的访问时间
# print(os.stat("d:/python"))
print(os.path.getctime("d:/python"))


# 得到指定文件最后一次的修改时间
print(os.path.getmtime("d:/python"))

# 得到指定文件大小 单位: 字节
print(os.path.getsize("d:/python/bilaisheng/base/def.py"))

# 测试参数是否为绝对路径
print(os.path.isabs("python_modules"))

# 测试参数是否为绝对路径
print(os.path.isabs("/bilaisheng"))

# 测试指定参数是否为一个文件
print(os.path.isfile("d:/python"))

# 测试指定参数是否为目录名
print(os.path.isdir("d:/python"))

# split 分割目录名, 返回由其目录名和基名给成的元祖
print(os.path.split("/tmp/foo.txt"))

# splitext 分割文件名，返回文件名和扩展名组成的元祖
print(os.path.splitext("/tmp/foo.txt"))

