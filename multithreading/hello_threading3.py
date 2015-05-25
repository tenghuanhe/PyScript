from time import ctime, sleep
import threading
from random import choice

class MyThread(threading.Thread):
  def __init__(self, func, args, name):
    super(MyThread, self).__init__();
    self.func = func
    self.args = args
    self.name = name
  def run(self):
    self.result = self.func(*self.args)

  def getResult(self):
    return self.result

def loop(number, sec):
  print "Thread ", number, " begins and will sleep", sec, " at ", ctime()
  sleep(sec)
  print "Thread ", number, " ends at ", ctime()

def main():
  seconds = [2, 4]
  threads = []
  
  for i in range(len(seconds)):
    t = MyThread(loop, (i, choice(seconds)), loop.__name__)
    threads.append(t)
  print "main Thread begins at ", ctime()
  
  for t in threads:
    t.start()
  for t in threads:
    t.join()
  
  print "main Thread ends at ", ctime()

if __name__ == "__main__":
  main()