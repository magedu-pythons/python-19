# 2、给出一个无序的整型列表，找出最长连续元素序列的长度，时间复杂度要求在线性时间内。
# 例如：
#     输入：[8,1,9,3,2,4]，那么其最长连续序列是[1,2,3,4]，即输出长度为4

def find_longest_consequence(array: list):
    if not array:
        return 0
    hashset = set(array)
    max_num = 0

    for i in array:
        if i - 1 not in hashset:
            j = i
            while i in hashset:
                i += 1
            max_num = max(max_num, i - j)

    return max_num


# test
print('Q2:', 80 * '-')
print(find_longest_consequence([8, 1, 9, 3, 2, 4, 5]))
