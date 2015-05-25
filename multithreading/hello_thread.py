#!/usr/bin/python
# -*- coding: utf-8 -*-

import thread
import time

def p_time( thread_name, delay):
  count = 0;
  while count < 5:
    # time.sleep(delay)
    count += 1
    print "%s %s" % (thread_name, time.ctime(time.time()))

def main():
  try:
    thread.start_new_thread( p_time, ("Thread1", 0.05, ))
    thread.start_new_thread( p_time, ("Thread2", 0.05, ))
  except:
    print "Error unable to start thead"

  print "TenghuanHe"
  time.sleep(1)
  print "ShufangHong"

if __name__ == "__main__":
  main()

