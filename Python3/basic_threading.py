#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 20:43:59 2018

@author: krish
"""

import threading
from queue import Queue
import time

print_lock = threading.Lock()

def exampleJob(worker):
    time.sleep(0.5)
    with print_lock:
        print(threading.currentThread.__name__,worker)

def threader():
    while True:
        worker = q.get()
        exampleJob(worker)
        q.task_done()

q = Queue()

for x in range(10):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()

start = time.time()

for worker in range(20):
    q.put(worker)

q.join()

print('Entire job took:',time.time()-start)
