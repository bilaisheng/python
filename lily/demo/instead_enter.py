# Filename : instead_enter.py
# Author by : Lily
# 用quit来代替回车结束程序


def file_write(file_n):
    f = open(file_n, 'w', encoding='utf-8')
    print('请输入内容【单独输入\'quit\'保存退出】')

    while True:
        file_content = input()
        if file_content != 'quit':
            f.write('%s\n' % file_content)
        else:
            break
    f.close()

file_n = input('请输入文件名：')
file_write(file_n)
