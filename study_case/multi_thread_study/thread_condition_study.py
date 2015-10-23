# coding=UTF-8

import threading
import time

__author__ = 'jubileus'

"""
    一个简单的生产消费者模型，通过条件变量的控制产品数量的增减，调用一次生产者产品就是+1，调用一次消费者产品就会-1.

    使用 Condition 类来完成，由于它也可以像锁机制那样用，所以它也有 acquire 方法和 release 方法，而且它还有
    wait， notify， notifyAll 方法。
"""


class Goods:  # 产品类
    def __init__(self):
        self.count = 0

    def add(self, num=1):
        self.count += num

    def sub(self):
        if self.count >= 0:
            self.count -= 1

    def empty(self):
        return self.count <= 0


class Producer(threading.Thread):  # 生产者类
    def __init__(self, condition, goods, sleep_time=1):  # sleep_time=1
        threading.Thread.__init__(self)
        self.cond = condition
        self.goods = goods
        self.sleep_time = sleep_time

    def run(self):
        cond = self.cond
        goods = self.goods
        while True:
            cond.acquire()  # 锁住资源
            goods.add()
            print("产品数量:", goods.count, "生产者线程")
            cond.notifyAll()  # 唤醒所有等待的线程--》其实就是唤醒消费者进程
            cond.release()  # 解锁资源
            time.sleep(self.sleep_time)


class Consumer(threading.Thread):  # 消费者类
    def __init__(self, condition, goods, sleep_time=2):  # sleep_time=2
        threading.Thread.__init__(self)
        self.cond = condition
        self.goods = goods
        self.sleep_time = sleep_time

    def run(self):
        cond = self.cond
        goods = self.goods
        while True:
            time.sleep(self.sleep_time)
            cond.acquire()  # 锁住资源
            while goods.empty():  # 如无产品则让线程等待
                cond.wait()
            goods.sub()
            print("产品数量:", goods.count, "消费者线程")
            cond.release()  # 解锁资源


g = Goods()
c = threading.Condition()

pro = Producer(c, g)
pro.start()

con = Consumer(c, g)
con.start()

con2 = Consumer(c, g)
con2.start()
