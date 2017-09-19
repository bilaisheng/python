import os

# 获取当前执行该文件的进程ID
print("Process (%s) start..." % os.getpid())


# multiprocessing 为可以跨平台版本的多进程模块
from multiprocessing import Process

import os


# 子进程要执行的代码
def run_proc(name):
    # 输出当前执行的名称以及进程ID
    print('Run child process %s (%s)' % (name, os.getpid()))

if __name__ == '__main__':
    # 输出当前父进程的进程ID
    print('Parent process %s ' % os.getpid())
    # 运行run_proc() 传递参数为test 当做run_proc中的name参数
    # 创建一个Process实例
    # Tips : target后 待执行方法不加() 直接方法名称
    p = Process(target=run_proc, args=('test',))
    print('Child process will start !')
    # 启动
    p.start()
    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    p.join()
    print('Child process end ! ')