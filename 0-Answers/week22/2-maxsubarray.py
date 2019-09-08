# 2、给出一个无序的列表（至少包含一个元素），求出其最大连续子列表的和？
#   举例：输入[−2,1,−3,4,−1,2,1,−5,4]，那么连续子列表[4,−1,2,1]有最大值，相加是 6

def max_sub_array_sum(array):
    length = len(array)
    max_so_far = array[0]
    current_max = array[0]
    for i in range(1, length):
        current_max = max(array[i], current_max + array[i])
        max_so_far = max(max_so_far, current_max)
    return max_so_far