# coding=UTF-8

import threading
import time

__author__ = 'jubileus'


class Num:
    def __init__(self):
        self.num = 0
        self.lock = threading.Lock()

    def add(self):
        self.lock.acquire()  # 加锁，锁住相应的资源
        self.num += 1
        num = self.num
        self.lock.release()  # 解锁，离开该资源
        return num


n = Num()


class JThread(threading.Thread):
    def __init__(self, t_id):
        threading.Thread.__init__(self)
        self.t_id = t_id

    def run(self):
        time.sleep(2)
        value = n.add()  # 将num加1，并输出原来的数据和+1之后的数据
        print('线程ID：{_t_id},   当前num:{_num}'.format(_t_id=self.t_id, _num=value))


for id in range(5):
    t = JThread(id)
    t.start()
    t.join()  # 使线程一个一个执行
