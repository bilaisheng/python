import os

filename = '15464657761111111.pdf'

pathDir = 'F:/tqcs/sr'

# 判断文件是否存在
if os.path.exists(pathDir + '/' + filename):
    print(filename + '文件在' + pathDir + '中存在 ! ')
else:
    # 打开文件,不存在则创建
    file = open('F:/tqcs/msmj.txt', 'wr')

    print(filename + '文件不存在sr目录下,将名字写入到msmj.txt文件中 ! ')

    # 将文件名写入到指定文件中
    file.write(filename)

    # 关闭
    file.close()
