#coding=gbk
#Python�е��̴߳��� 
''' 
Python�жԶ��߳����������������� 
һ����threadģ���start_new_thread���������߳�������һ������������ú�������ֵ��Ϊ���ѣ�Python�ٷ����Ƽ� 
��һ���Ǽ���threadingģ���Thread�࣬Ȼ����дrun������������Java��Runnable�ӿڶ��壬����Խϸ� 
''' 
print "=======================thread.start_new_thread�����߳�=============" 
import thread 
#Python���߳�sleep������������threadģ���У���������timeģ���� 
import time 
def inthread(no, interval): 
  count = 0 
  while count<10: 
    print "Thread-%d,���߼����%d,current Time:%s"%(no, interval, time.ctime()) 
#ʹ��ǰ�߳�����ָ��ʱ�䣬intervalΪ�����͵���������ͬ��Java�е����κ����� 
    time.sleep(interval) 
#Python���������߼�����һ��֧��++��������ֻ����+=ʵ�� 
    count += 1 
  else: 
    print "Thread-%d is over"%no 
#���Եȴ��̱߳�PVM���գ�����������exit��exit_thread���������߳� 
    thread.exit_thread() 
#ʹ��start_new_thread�������Լ򵥵�����һ���߳�,��һ������ָ���߳���ִ�еĺ������ڶ�������ΪԪ���͵Ĵ��ݸ�ָ�������Ĳ���ֵ 
thread.start_new_thread(inthread,(1,2)) 
#�߳�ִ��ʱ���������һ�У�����sleep��ʱ������㹻ʹ�߳̽������籾�� 
#�������ʱ���Ϊ20�������ܻ��׳��쳣 
time.sleep(30) 
''' 
ʹ�����ַ��������߳�ʱ���п��ܳ����쳣Unhandled exception in thread started by 
Error in sys.excepthook: 

Original exception was: 
����������߳�֮�󣬱������time.sleep�����㹻����ʱ�䣬ʹ���̵߳ȴ��������̷߳��ؽ����������̱߳����߳���������ͻ��׳�����쳣 
''' 

