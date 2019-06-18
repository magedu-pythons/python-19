# 1、使用Python实现一个双端队列
class DoubleEndedQueue:
    def __init__(self, length=10):  # 0-9 0-4|5-9
        self.body = [0] * length
        self.length = length
        self.ins_length = 0
        self.head = length // 2 - 1
        self.tail = length // 2

    def insert_left(self, value):
        if self.head == -1:
            print('left is full')
            return
        self.body[self.head] = value
        self.head -= 1

    def pop_left(self):
        if self.head == self.length // 2 - 1:
            print('left is empty')
            return
        res = self.body[self.head + 1]
        self.head += 1
        return res

    def insert_right(self, value):
        if self.tail == self.length:
            print('right is full')
            return
        self.body[self.tail] = value
        self.tail += 1

    def pop_right(self):
        if self.tail == self.length // 2:
            print('right is empty')
            return
        res = self.body[self.tail - 1]
        self.tail -= 1
        return res

    def print_q(self):
        print(self.body[self.head + 1:self.tail])


# test
d = DoubleEndedQueue()
d.pop_left()
d.pop_right()
d.insert_left('add1')
d.print_q()
d.insert_left('add2')
d.print_q()
d.insert_right('add3')
d.insert_right('add4')
d.insert_right('add5')
d.insert_right('add6')
d.insert_right('add7')
d.insert_right('add8')
d.insert_right('add9')
print(d.pop_right())
print(d.pop_left())
d.print_q()

# 2、输入n 个整数，输出其中最小的k 个。
# 例如输入1，2，3，4，5，6，7 和8 这8 个数字，则最小的4 个数字为1，2，3 和4
