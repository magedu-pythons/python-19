# 1、实现数据结构stack(栈)，并实现它的append，pop方法【动手查询相关资料理解stack特点以及与queue区别】
# stack 是先进后出数据结构 进：1->2->3  出：<-1<-2<-3
# queue 是先进先出数据结构 进：1->2->3  出：<-3<-2<-1


class Node:
    def __init__(self, value):
        self.value = value
        self._next = None

    def get_next(self):
        return self._next

    def set_next(self, node):
        self._next = node


class Stack:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.head is None:
            return
        tmp = self.head
        node = self.head.get_next()
        self.head = node
        return tmp.value


# test
l1 = [1, 5, 3, 2, 5, 6]
stack = Stack()
for x in l1:
    stack.append(x)

for y in l1:
    print(stack.pop())
