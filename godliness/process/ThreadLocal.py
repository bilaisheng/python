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
t1 = threading.Thread(target= process_thread, args=('Memor',),name= 'Thread-A')


# 声明一个名字为:Thread-B的线程 执行process_thread方法 传入name为Godliness
# Tips: 此处传入的target的方法名称不需要加() 
t2 = threading.Thread(target= process_thread, args=('Godliness',),name= 'Thread-B')
	
# 启动    
t1.start()
t2.start()
t1.join()
t2.join()