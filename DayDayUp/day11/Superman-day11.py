# 多进程
# Unix、Linux操作系統提供了fork系統調用。普通函數調用，調用一次返回一次，但是fork調用一次，返回兩次。
# 因為操作系統自動把當前進程父進程複製了一份子進程，然後分別在父進程和子進程內返回。子進程永遠返回0，而
# 父進程返回子進程的ID。這樣一個父進程可以fork出很多子進程。所以，父進程只要記下每個子進程的Id，而子進程只要
# getppid就可以拿到父進程的Id。
import os
# print('Process (%s) start ...' % os.getppid())
# pid = os.fork()
# print(pid)
# multiprocessing
from multiprocessing import Process


def run_proc(name):
    print('run child process %s (%s)...' % (name, os.getppid()))
    if __name__ == '__main__':
        print('parent process %s (%s)...' % (name,os.getppid()))
        p = Process(target=run_proc, args=('test',))
        print('Chlid process will start.')
        p.start()
        p.join()
        print('child process end.')
# run_proc()
# pool
# 若要啟動大量的子進程，可以用進程池
import os, time , random
from  multiprocessing import Pool


def long_time_task(name):
    print('run task (%s)...' % (name, os.getppid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))
if __name__=='__main__':
    print('parent process %s.' % os.getppid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('waiting for all subprocess done.')
    p.close()
    p.join()
    print('all subprocess done.')
# 子進程
import subprocess
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
print('exit code:', p.returncode)

# 進程之間的通信
# Queue
from multiprocessing import  Process,Queue
import os, time, random


def write(q):
    print('process to write:%s' % os.getppid())
    for value in ['A', 'B', 'C']:
        print('put %s to queue..' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('process to read: %s' % os.getppid())
    while True:
        value = q.get(True)
        print('get %s from queue' % value)

if __name__ == '__main__':
    q=Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()


# 多线程
# 多任务可以由多进程完成，也可以由一个进程内的多线程完成,一個進程至少有一個線程。
# python 的標準庫提供了兩個模塊：_thread和threading,前者是低級模塊，後者是高級模塊，並且對前者進行了封裝。
import time, threading


# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
        print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
# Lock
# 多線程和多進程最大的區別是同一個變量，各自拷貝到買一個進程中，互不影響，而多線程
# 所有變量都由所有線程共享，存在危險多線程同時修改一個變量
balance = 0


def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        change_it(n)
t1 = threading.Thread(target=run_thread, args=(5, ))
t2 = threading.Thread(target=run_thread, args=(8, ))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
# 要確保變量不變化必須要枷鎖
lock = threading.Lock


def run_thread(n):
    lock.acquire()  # 多個線程執行lock.acquire()只有一個線程能夠成功獲取鎖
    for i in range(100000):
        try:
            change_it(n)
        finally:
            lock.release()


# ThreadLocal
# 在多線程環境下，買一個線程都有自己的數據，一個線程使用自己的局部變量畢使用全局變量好。
class Student(object):
    name =object.__name__

# 每個函數調用都要傳入，不方便


def peocess_student(name):
    std = Student(name)
    do_subtask_1(std)
    do_subtask_2(std)


def do_subtask_1(std):
    do_subtask_1(std)
    do_subtask_2(std)


def do_subtask_2(std):
    do_subtask_2(std)
    do_subtask_2(std)

global_dict ={}


def std_thread(name):
    std = Student(name)
    global_dict[threading.current_thread()]
    do_task_1()
    do_task_2()


def do_task_1():
    std = global_dict[threading.current_thread()]


def do_task_2():
    std = global_dict[threading.current_thread()]
# ThreadLocal對象可以實現這個效果
local_school = threading.local()


def process_student():
    std = local_school.student
    print('hello, %s(in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    process_student()
t1 = threading.Thread(target=process_thread, args=('Alice', ), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob', ), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
# 进程 vs. 线程
# 實現多任務，通常會上級Master-Worker模式，Master負責分配任務，Worker負責執行任務，因此多任務下通常是一個Master多個Worker
# 若使用多進程實現，主進程是Master，其他進程Worker
# 若使用多線程實現， 主線程就是Master，其他線程就是worker
# 多進程的方式優點就是穩定性高，一個子進程崩潰了不會影響到其他子進程，但是缺點就是開銷巨大。操作系統的同時運行進程數也是有限的。
# 多線程比進程快一點，但是多線程模式的最大缺點就是任何一個線程掛掉都有可能導致整個進程崩潰。

# 任務類型：計算密集型和IO密集型
# 计算密集型任务由于主要消耗CPU资源，因此，代码运行效率至关重要。Python这样的脚本语言运行效率很低，完全不适合计算密集型任务。对于计算密集型任务，最好用C语言编写
# 第二种任务的类型是IO密集型，涉及到网络、磁盘IO的任务都是IO密集型任务，这类任务的特点是CPU消耗很少，任务的大部分时间都在等待IO操作完成（因为IO的速度远远低于CPU和内存的速度）。
# 对于IO密集型任务，任务越多，CPU效率越高，但也有一个限度。常见的大部分任务都是IO密集型任务，比如Web应用。適合代碼少的語言
# 現代的操作系統支持一步IO

# 分布式进程
# 在Thread和process中，應當首選Process ，因為Process穩定一些，並且Process可以發佈在多台机器上而Thread只能分布在同一台机器上的多个cpu上
# 服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务
# task_master.py
import random, time , queue
from multiprocessing.managers import BaseManager
task_queue = queue.Queue()
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass
QueueManager.register('get_task_queue', callable=lambda :task_queue)
QueueManager.register('get_result_queue', callable=lambda :result_queue)
manager = QueueManager(adress=('', 5000), authkey=b'abc')
manager.start()
task = manager.get_task_queue()
result = manager.get_result_queue()
for i in range(10):
    n = random.readint(0, 10000)
    print('Put task %d..' % n)
    task.put(n)
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
manager.shutdown()
print('master exit.')
# 另一台机器上启动任务进程
# task_worker.py
# 创建类似的QueueManager:


class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行task_master.py的机器:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接:
m.connect()
# 获取Queue的对象:
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
# 处理结束:
print('worker exit.')

