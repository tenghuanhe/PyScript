#coding=utf-8
import thread;
from time import sleep,ctime;

a = [1, 1]

def loop(nloop,sec):
  global a
  print "Thread ", nloop, " start and will sleep ", sec
  sleep(sec)
  print "Thread ", nloop, " end  ", sec
  a[nloop] = 0

def main():
  global a
  seconds=[4,2]

  print "main Thread begins:", ctime()
  for i in range(len(seconds)):
    thread.start_new_thread(loop,(i,seconds[i]))
  while sum(a): 
    pass
  print "main Thread ends:",ctime()

if __name__=="__main__" :
  main()
'''
通过加入锁机制，可以来避免出现由于主线程提前退出导致子线程中断而抛出中断异常
'''
