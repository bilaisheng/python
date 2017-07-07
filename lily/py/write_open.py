#!/usr/bin/python3
# Filename : write_open.py
# Author by : Lily

# 写文件
with open("test.txt","wt") as out_file:
    out_file.write("该文本会写入到文件中\n看到我了吧！")

# Read a file
with open("test.txt","rt") as in_file:
    text = in_file.read()

print(text)