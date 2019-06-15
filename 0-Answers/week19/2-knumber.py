# 2、输入n 个整数，输出其中最小的k 个。
# 例如输入1，2，3，4，5，6，7 和8 这8 个数字，则最小的4 个数字为1，2，3 和4。
import heapq


def find_k_min_numbers(array, k):
    k_array = heapq.nsmallest(k ,array)
    return k_array

def find_k_min_numbers2(array, k):
    array.sort()
    return array[:k]
