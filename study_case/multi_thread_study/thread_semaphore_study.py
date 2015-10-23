# coding=UTF-8

import threading
import time

__author__ = 'jubileus'


class Num:
    def __init__(self):
        self.num = 0
        self.sem = threading.Semaphore(value=3)
        # 允许最多三个线程同时访问资源

    def add(self):
        self.sem.acquire()  # 内部计数器减1
        self.num += 1
        num = self.num
        self.sem.release()  # 内部计数器加1
        return num


n = Num()


class JThread(threading.Thread):
    def __init__(self, t_id):
        threading.Thread.__init__(self)
        self.t_id = t_id

    def run(self):
        time.sleep(2)
        value = n.add()
        print('线程ID：{_t_id},   当前num:{_num}'.format(_t_id=self.t_id, _num=value))


for id in range(5):
    t = JThread(id)
    t.start()
    t.join()
