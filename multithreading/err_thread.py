#coding=gbk
#Python中的线程处理 
''' 
Python中对多线程有两种启动方法： 
一种是thread模块的start_new_thread方法，在线程中运行一个函数，但获得函数返回值极为困难，Python官方不推荐 
另一种是集成threading模块的Thread类，然后重写run方法，类似于Java的Runnable接口定义，灵活性较高 
''' 
print "=======================thread.start_new_thread启动线程=============" 
import thread 
#Python的线程sleep方法并不是在thread模块中，反而是在time模块下 
import time 
def inthread(no, interval): 
  count = 0 
  while count<10: 
    print "Thread-%d,休眠间隔：%d,current Time:%s"%(no, interval, time.ctime()) 
#使当前线程休眠指定时间，interval为浮点型的秒数，不同于Java中的整形毫秒数 
    time.sleep(interval) 
#Python不像大多数高级语言一样支持++操作符，只能用+=实现 
    count += 1 
  else: 
    print "Thread-%d is over"%no 
#可以等待线程被PVM回收，或主动调用exit或exit_thread方法结束线程 
    thread.exit_thread() 
#使用start_new_thread函数可以简单的启动一个线程,第一个参数指定线程中执行的函数，第二个参数为元组型的传递给指定函数的参数值 
thread.start_new_thread(inthread,(1,2)) 
#线程执行时必须添加这一行，并且sleep的时间必须足够使线程结束，如本例 
#如果休眠时间改为20，将可能会抛出异常 
time.sleep(30) 
''' 
使用这种方法启动线程时，有可能出现异常Unhandled exception in thread started by 
Error in sys.excepthook: 

Original exception was: 
解决：启动线程之后，必须调用time.sleep休眠足够长的时间，使主线程等待所有子线程返回结果，如果主线程比子线程早结束，就会抛出这个异常 
''' 

