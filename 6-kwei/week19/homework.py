# 1、请实现一个生产者、消费者的模型，生产者随机生成N对数据，消费者对这N对数据进行加法运算，并将计算出结果记录到本地文件，任务完成时，屏幕打印出 “run sucesss”，并结束程序。
# 例如：生产者生成数字1，5，消费者计算1+5=6，将运算结果6保存到本地文件中。

# 3000对数据
# 队列大小100

import queue
import random
import threading

q = queue.Queue(maxsize=100)
lock = threading.Lock()


class Producer:
    def __init__(self, total=3000):
        self.total = total
        self.q = q
        self.lock = lock

    def start(self):
        for _ in range(self.total):
            self.q.put([random.randint(1, 100) for _ in range(2)])


class Consumer:
    def __init__(self):
        self.q = q
        self.lock = lock

    def start(self):
        file = open('test', 'w+')
        with file:
            while not q.empty():
                res = self.q.get(block=True, timeout=0.1)
                if res:
                    file.write('{}\n'.format(res[0]+res[1]))


p = Producer()
c = Consumer()

threading.Thread(target=p.start, name='producer').start()
threading.Thread(target=c.start, name='consumer').start()


# 2、请实现Python中数据结构dict，要求实现字典的get、set（key,value赋值）方法


class MyDict:
    def __init__(self):
        self.dict = {}

    def set(self, key, value):
        self.dict[key] = value

    def get(self, key):
        return self.dict[key]

    def __str__(self):
        return str(self.dict)

    __repr__ = __str__


d = MyDict()
d.set('arg1', 122)
print(d.get('arg1'))
print(d)
