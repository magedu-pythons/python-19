# 1、使用归并排序、插入排序算法对列表进行排序

# 1) merge sort:----------------------------------------------
import random
from typing import List

arr = [random.randint(1, 100) for _ in range(20)]
print('origin:', arr)


def merge_sort(arr: List[int]):
    merge_sort_c(arr, 0, len(arr) - 1)


def merge_sort_c(arr: List[int], low: int, high: int):
    if low < high:
        mid = (low + high) // 2
        merge_sort_c(arr, low, mid)
        merge_sort_c(arr, mid + 1, high)
        merge(arr, low, mid, high)


def merge(arr: List[int], low: int, mid: int, high: int):
    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:  # 归并排序的精髓就是在合并的时候顺便排序
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(arr[start:end + 1])
    arr[low:high + 1] = tmp


merge_sort(arr)
print('merge sort:', arr)

# 2) insertion sort:----------------------------------------------
arr = [random.randint(1, 100) for _ in range(20)]
print('origin', arr)
arr = [0] + arr


def insertion_sort(arr):
    length = len(arr)
    for i in range(1, length):
        arr[0] = arr[i]
        j = i - 1
        if arr[j] > arr[0]:
            while arr[j] > arr[0]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = arr[0]  # 关键要注意j的位置, 插入的位置应该是j+1


insertion_sort(arr)
print('insertion', arr[1:])

# 2、实现一个LRU缓存类，至少包含get和put方法 
"""
    我的思路是这样的：我们维护一个有序单链表，越靠近链表尾部的结点是越早之前访问的。
    当有一个新的数据被访问时，我们从链表头开始顺序遍历链表。
    1. 如果此数据之前已经被缓存在链表中了，
        我们遍历得到这个数据对应的结点，并将其从原来的位置删除，然后再插入到链表的头部。
    2. 如果此数据没有在缓存链表中，又可以分为两种情况：
        如果此时缓存未满，则将此结点直接插入到链表的头部；
        如果此时缓存已满，则链表尾结点删除，将新的数据结点插入链表的头部。
"""


class LrcLinkedList:
    def __init__(self, length: int = 10):
        self.length = length  # all length
        self.instlength = 0  # instance length
        self.lrcspace = None

    def put(self, data, pos):  # 将数据插入当前的n位置, 若果pos过大, 默认加在末尾
        if self.lrcspace is None:
            self.lrcspace = LinkedNode(data)
            self.instlength += 1
            return
        if pos > self.instlength:  # 若果pos过大, 默认加在末尾
            p = self.lrcspace
            while p.nextnode is not None:
                p = p.nextnode
            p.nextnode = LinkedNode(data)
            self.instlength += 1
            return
        if pos <= 1:  # 若pos <= 1, 默认加载开头
            newnode = LinkedNode(data)
            newnode.nextnode = self.lrcspace
            self.lrcspace = newnode
            self.instlength += 1
            return
        p = self.lrcspace
        for _ in range(pos - 2):
            p = p.nextnode
        newnode = LinkedNode(data)
        newnode.nextnode = p.nextnode
        p.nextnode = newnode
        self.instlength += 1

    def delete(self, pos):  # 将链表的第几个节点删除
        if self.lrcspace is None:
            print('empty!')
            return
        if pos <= 1:
            p = self.lrcspace
            self.lrcspace = self.lrcspace.nextnode
            del p
            self.instlength -= 1
            return
        if pos > self.instlength:
            if self.instlength == 1:
                p = self.lrcspace
                self.lrcspace = self.lrcspace.nextnode
                del p
                self.instlength -= 1
            p = self.lrcspace
            while p.nextnode.nextnode is not None:
                p = p.nextnode
            pdel = p.nextnode
            p.nextnode = p.nextnode.nextnode
            del pdel
            self.instlength -= 1
            return
        p = self.lrcspace
        for _ in range(pos - 2):
            p = p.nextnode
        pdel = p.nextnode
        p.nextnode = p.nextnode.nextnode
        del pdel
        self.instlength -= 1
        return

    def get(self, data):
        if self.lrcspace is None:
            self.lrcspace = LinkedNode(data)
            self.instlength += 1
            return
        p = self.lrcspace
        count = 1
        while p.data != data:
            p = p.nextnode
            if p is not None:
                count += 1
            if p is None:  # 遍历完了却没找到
                if self.instlength < self.length:
                    self.put(data, 1)
                else:
                    self.delete(self.length)
                    self.put(data, 1)
                return
        # 找到了
        self.delete(count)
        self.put(data, 1)
        return


class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.nextnode = None


def printlist(linkedlist):
    tempointer = linkedlist.lrcspace
    count = 1
    if tempointer is None:
        print("---node null, data = null.---")
        return
    while tempointer.nextnode is not None:
        print("---node {}, data = {}, {}th node, whole length = {}.---".format(count,
                                                                               tempointer.data,
                                                                               count,
                                                                               linkedlist.length))
        count += 1
        tempointer = tempointer.nextnode
    print("---node {}, data = {}, {}th node, whole length = {}.---".format(count,
                                                                           tempointer.data,
                                                                           count,
                                                                           linkedlist.length))


#  test
l = LrcLinkedList(4)
printlist(l)
l.get('data1')
l.get('data1')
printlist(l)
print('---')
l.get('data2')
l.get('data3')
l.get('data1')
l.get('data5')
l.get('data2')
l.get('data5')
printlist(l)
