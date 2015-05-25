#coding=utf-8
import thread
from time import sleep, ctime
from random import choice
#The first param means the thread number
#The second param means how long it sleep
#The third param means the Lock
def loop(nloop,sec,lock):
  print "Thread ", nloop, " start and will sleep ", sec
  sleep(sec)
  print "Thread ", nloop, " end  ", sec
  lock.release()

def main():
  seconds=[4,2]
  locks=[]
  for i in range(len(seconds)):
    lock=thread.allocate_lock()
    lock.acquire()
    locks.append(lock)
        
  print "main Thread begins:",ctime()
  for i,lock in enumerate(locks):
    thread.start_new_thread(loop,(i,choice(seconds),lock))
  for lock in locks:
    while lock.locked():
      pass
  print "main Thread ends:",ctime()

if __name__=="__main__" :
  main()
'''
通过加入锁机制，可以来避免出现由于主线程提前退出导致子线程中断而抛出中断异常
'''
