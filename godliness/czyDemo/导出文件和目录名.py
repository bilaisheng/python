#导出当前目录下的所有文件和目录名
#导入OS模块
import os
#os.listdir 可以列出文件和目录
a = [d for d in os.listdir('.')]
print(a)