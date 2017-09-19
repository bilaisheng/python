
# 当在import一个模块的时候,Python会寻找几个地方.
# 具体来说,它会搜寻在sys.path里面定义的所有目录.

# 通过添加一个目录名称到sys.path里,可以在运行时添加一个新的目录到Python
# 的搜索路径中,然后无论任何时候你想导入一个模块,Python都会同样的去查找
# 那个目录.只要python还在运行,都会一直有效.

# 通过使用sys.path.insert(0,new_path),可以插入一个新的目录到sys.path列
# 表的第一项,从而使其出现在Python搜索路径的开头.
import sys

print(sys.path)