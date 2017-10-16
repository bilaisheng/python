# 创建子进程
# multiprocessing模块就是跨平台版本的多进程模块
# multiprocessing模块提供了一个Process类来代表一个进程对象
# from multiprocessing import Process
# import os
#
#
# # 子进程要执行的代码
# def run_proc(name):
#     print('子进程运行 %s (%s)...' % (name, os.getpid()))
#
# if __name__=='__main__':
#     print('父进程 %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('子进程将要开始运行')
#     p.start()
#     p.join()
#     print('子进程结束.')
#
# '''
# 上面的例子中：
#     创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动
#     join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
# '''
#
# # 用进程池的方式批量创建子进程
# from multiprocessing import Pool
# import os, time, random
#
#
# def long_time_task(name):
#     print('任务运行 %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('任务 %s 执行了 %0.2f 秒.' % (name, (end - start)))
#
# if __name__=='__main__':
#     print('子进程 %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('等待所有的子进程执行...')
#     p.close()
#     p.join()
#     print('所有进程执行完毕.')

'''
说明：
    p = Pool(4) 相当于创造5个进程，有5个进程在跑，注意pool在电脑上面是
    有一个默认值的，请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4
    要等待前面某个task完成后才执行（由于Pool的默认大小是CPU的核数）
    
'''

# # 控制子进程的输入和输出
# import subprocess
#
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)
#
# # 如果子进程还需要输入，则可以通过communicate()方法输入
# import subprocess
#
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)

# 进程之间的通信
# Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。

# from multiprocessing import Process,Queue
# import os, time, random
#
#
# # 写数据进程的方法
# def write(q):
#     print('进程开始写数据 %s'% os.getpid())
#     for value in['A','B','C']:
#         print('put %s to queue'%value)
#         q.put(value)
#         time.sleep(random.random())
#
#
# # 读数据进程的方法
# def read(q):
#     print('进程开始读取数据 %s'% os.getpid())
#     while True:
#         value = q.get(True)
#         print('%s 进程获取数据%s'%(value, os.getpid()))
#
# if __name__ == '__main__':
#     # 父进程创建queue ,并传给各个子进程
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#
#     # 启动子进程pw写入数据
#     pw.start()
#     # 启动子进程pr读取数据
#     pr.start()
#     # 等待pw结束
#     pw.join()
#     # 因为子进程pr是死循环，无法等待期自动结束所以要强制终止
#     pr.terminate()

'''
多线程
Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，
对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
'''
# import time, threading
#
#
# # 新线程执行的代码
# def loop():
#     print('进程 %s 正在执行。。。'% threading.current_thread().name)   # current_thread()函数，永远返回当前线程的实例
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)   # 进程等待时间
#     print('thread %s ended.' % threading.current_thread().name)
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='测试')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

'''
多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份
拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程
共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间
共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了
'''
import time, threading

# 假定这是你的银行存款:
# balance = 0

#
# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n


# def run_thread(n):
#     for i in range(1000000):
#         change_it(n)
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# 理论上上面的例子应该是得到0的，但是由于两个线程交替执行导致balance的结果不一定为0
# 原因是因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算balance = balance + n，也分两步：
# 计算balance + n，存入临时变量中；将临时变量的值赋给balance
# 究其原因，是因为修改balance需要多条语句，而执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象的内容改乱了。

'''
就要给change_it()上一把锁，当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，因此其他线程不能同时
执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。由于锁只有一个，无论多少线程，同一时刻最多只有
一个线程持有该锁，所以，不会造成修改的冲突。创建一个锁就是通过threading.Lock()来实现
'''
# balance = 0
# lock = threading.Lock()
#
#
# def run_thread(n):
#     for i in range(100000):
#         # 先要获取锁:
#         lock.acquire()   # 当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。
#         try:
#             # 放心地改吧:
#             print('%s 正在使用锁'% threading.current_thread().name)
#             change_it(n)
#         finally:
#             # 改完了一定要释放锁:
#             print('%s 释放了锁'% threading.current_thread().name)
#             lock.release()
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('balance 的结果是%s'%balance)

'''
总结：
在多线程环境下，每个线程都有自己的数据。一个线程使用
自己的局部变量比使用全局变量好，因为局部变量只有线程
自己能看见，不会影响其他线程，而全局变量的修改必须加锁

而局部变量的的麻烦在于函数调用的时候
'''

'''
分布式进程：
    在Thread和Process中，应当优选Process，因为Process更稳定，
    而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。

    Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布
    到多台机器上。一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通
    信。由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。
'''
import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()


# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue:
manager.start()
# 获得通过网络访问的Queue对象:
# 当我们在一台机器上写多进程程序时，创建的Queue可以直接拿
# 来用，但是，在分布式多进程环境下，添加任务到Queue不可以
# 直接对原始的task_queue进行操作，那样就绕过了QueueManager
# 的封装，必须通过manager.get_task_queue()获得的Queue接口添加
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去:
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# 从result队列读取结果:
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
# 关闭:
manager.shutdown()
print('master exit.')






