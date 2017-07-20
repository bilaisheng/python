#!/usr/bin/python3
# Filename : sub_test.py
# Author by : Lily

import re
phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码：",num)
# 移除非数字内容
num = re.sub(r'\D', "", phone)
print("电话号码：", num)
