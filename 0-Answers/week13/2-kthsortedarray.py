# 2、两个有序数组，分别拥有m和n的长度，求其合并后的第k个值

def find_kth_sorted_arrays_1(arr_a, arr_b, k):
    m = len(arr_a)
    n = len(arr_b)
    s1 = [0] * (m + n)
    i, j, d = 0, 0, 0

    while i < m and j < n:
        if arr_a[i] < arr_b[j]:
            s1[d] = arr_a[i]
            i += 1
        else:
            s1[d] = arr_b[j]
            j += 1
        d += 1

    while i < m:
        s1[d] = arr_a[i]
        d += 1
        i += 1

    while j < n:
        s1[d] = arr_b[j]
        d += 1
        j += 1
    print(s1)
    return s1[k - 1]


# test
a1 = [2, 3, 6, 7, 9, 14, 15]
b1 = [1, 4, 8, 10]
k1 = 8
print(find_kth_sorted_arrays_1(a1, b1, k1))
