from multiprocessing import Pool

import os
import time
import random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    # 开始时间
    start =time.time()
    time.sleep(random.random()*3)
    # 结束时间
    end =time.time()
    print('Task runs %0.2f seconds.' % (name, (end - start)))

if  __name__ == '__main__':
    print('Parent process %s. ' % os.getpid())
    # Pool(number) number为当前可以【同时】跑多少个进程
    # 由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('Waiting for all subprocess done...')

    # 调用close() 之后就不能继续添加新的Process了
    p.close()
    # 调用join() 之前必须先调用close()
    p.join()
    print('All suprocess done.')

    if __name__ == '__main__':
        print('Parent process %s.' % os.getpid())
        p = Pool(4)
        for i in range(5):
            p.apply_async(long_time_task, args=(i,))
        print('Waiting for all subprocesses done...')
        p.close()
        p.join()
        print('All subprocesses done.')