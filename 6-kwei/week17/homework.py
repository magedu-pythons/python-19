# 1、请实现一个方法将链表反转
# 举例：
# 链表a，有节点1->2->3->4  反转后为：4->3->2->1

# 实现一个具有插入和反转方法的单向链表


class SingleNode:
    def __init__(self, data=None, _next=None):
        self.data = data
        self._next = _next


class SingleLinkedList:
    def __init__(self):
        self.space = None
        self.len = 0

    def add(self, data):
        newnode = SingleNode(data)
        if not self.space:
            self.space = newnode
            return
        p = self.space
        while p._next:
            p = p._next
        p._next = newnode
        self.len += 1

    def reverse(self):
        if not self.space:
            return -1
        reverse_head = None
        head = self.space
        while head:
            next = head._next
            head._next = reverse_head
            reverse_head = head
            head = next
        self.space = reverse_head

    # A -> B -> C

    def __repr__(self):
        lst = []
        p = self.space
        while p:
            lst.append(str(p.data))
            p = p._next
        return '->'.join(lst)

    __str__ = __repr__


# test
l = SingleLinkedList()
for i in range(4):
    l.add(i)
print(l)
l.reverse()
print(l)


# 2、实现pow函数，分析其时间复杂度


def mypow(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1.0 / mypow(x, -n)
    else:
        half = mypow(x, n >> 1)
        if 0 == n % 2:
            return half * half
        else:
            return x * half * half


print(mypow(1.5, 2))
