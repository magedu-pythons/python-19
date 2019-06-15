# 1、使用归并排序、插入排序算法对列表进行排序

# merge sort:----------------------------------------------
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

# insertion sort:----------------------------------------------
arr = [random.randint(1, 100) for _ in range(20)]
print('origin', arr)
arr = [0] + arr


def insertion(arr):
    length = len(arr)
    for i in range(1, length):
        arr[0] = arr[i]
        j = i - 1
        if arr[j] > arr[0]:
            while arr[0] < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = arr[0]  # 关键要注意j的位置, 插入的位置应该是j+1


insertion(arr)
print('insertion', arr[1:])

# 2、实现一个LRU缓存类，至少包含get和put方法 
