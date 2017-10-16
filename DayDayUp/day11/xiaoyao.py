# 多进程
# 多线程
# Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程：
from multiprocessing import Pool
import os

# print("process (%s) start..." % os.getpid())
# pid = os.fork()
# if pid ==0:
# 	print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

import time
import random


def long_time_mission(name):
    print('run mission %s (%s)...' % (name, os.getpid()))
    # 开始时间
    start = time.time()
    time.sleep(random.random() * 3)
    # 结束时间
    end = time.time()
    print('mission runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
    print('Parent process %s. ' % os.getpid())
    # Pool(number) number为当前可以【同时】跑多少个进程
    # 由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_mission, args=(i,))
    print('waiting for all subprocess done...')

    # 调用close()之后就不能继续添加新的Process了
    p.close()
    # 调用join() 之前必须先调用close()
    p.join()
    print('All subprocess done...')
    
import os

# 获取当前执行该文件的进程ID
print("Process (%s) start..." % os.getpid())


# multiprocessing 为可以跨平台版本的多进程模块
from multiprocessing import Process

import os


# 子进程要执行的代码
def run_proc(name):
	#输出当前执行的名称以及进程ID
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
    print('Child process end !')

import threading

# Tips:一个ThreadLocal变量虽然是全局变量，
# 但每个线程都只能读写自己线程的独立副本，互不干扰。
# ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。

# 创建全局ThreadLocal对象
local_school = threading.local()


def process_student():
	# 获取当前线程关联的student:
	std = local_school.student
	print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
	# 绑定 TheadLocal的Student
	local_school.student = name
	# 调用上面的方法
	process_student()


# 声明一个名字为:Thread-A的线程 执行process_thread方法 传入name为Memor
# Tips: 此处传入的target的方法名称不需要加()
t1 = threading.Thread(target=process_thread, args=('Memor',), name='Thread-B')

# 声明一个名字为:Thread-B的线程 执行process_thread方法 传入name为Godliness
# Tips: 此处传入的target的方法名称不需要加()
t2 = threading.Thread(target=process_thread, args=('Xiaoyao',), name='Thread-B')

# 启动
t1.start()
t2.start()
t1.join()
t2.join()
