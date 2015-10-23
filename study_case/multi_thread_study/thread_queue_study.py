# coding=UTF-8

import threading
import queue
import time

__author__ = 'jubileus'

'''
1.创建一个 Queue.Queue() 的实例，然后使用数据对它进行填充。
2.将经过填充数据的实例传递给线程类，后者是通过继承 threading.Thread 的方式创建的。
3.每次从队列中取出一个项目，并使用该线程中的数据和 run 方法以执行相应的工作。
4.在完成这项工作之后，使用 queue.task_done() 函数向任务已经完成的队列发送一个信号。
5.对队列执行 join 操作，实际上意味着等到队列为空，再退出主程序。
'''


class JThread(threading.Thread):
    def __init__(self, index, queue):
        threading.Thread.__init__(self)
        self.index = index
        self.queue = queue

    def run(self):
        while True:
            time.sleep(1)
            item = self.queue.get()
            if item is None:
                break
            print("线程：", self.index, "任务", item, "完成")
            self.queue.task_done()  # task_done方法使得未完成的任务数量-1


q = queue.Queue(0)

'''
初始化函数接受一个数字来作为该队列的容量，如果传递的是
一个小于等于0的数，那么默认会认为该队列的容量是无限的.
'''

for i in range(2):
    JThread(i, q).start()  # 两个线程同时完成任务

for i in range(10):
    q.put(i)  # put方法使得未完成的任务数量+1
