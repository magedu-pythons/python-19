# 1、请实现一个生产者、消费者的模型，生产者随机生成N对数据，
# 消费者对这N对数据进行加法运算，并将计算出结果记录到本地文件，任务完成时，屏幕打印出 “run sucesss”，并结束程序。
# 例如：生产者生成数字1，5，消费者计算1+5=6，将运算结果6保存到本地文件中。
import threading
import random
import queue


def producer(number, q):
    for i in range(number):
        q.put((random.randint(1, 1000), random.randint(1, 1000)))


class Consumer(threading.Thread):

    def __init__(self, q, func):
        super().__init__()
        self.queue = q
        self.func = func

    def run(self):
        while True:
            args = self.queue.get()
            self.execute(*args)
            self.queue.task_done()

    def execute(self, *args):
        ret = self.func(*args)
        ret = '{}+{}={}\n'.format(*args, ret)
        with open('result.txt', 'a') as f:
            f.write(ret)


def run_task():
    def add(a, b):
        return a + b

    q = queue.Queue()
    for i in range(5):
        c = Consumer(q, func=add)
        c.setDaemon(True)
        c.start()

    producer(20, q)
    q.join()
    print('run success')
