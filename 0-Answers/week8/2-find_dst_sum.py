# 给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值
# 如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11
#


def find_dst_value(target: int, targets: list):
    """
    time complexity O(N^2)
    :param target:
    :param targets:
    :return:
    """
    length = len(targets)
    for i in range(length):
        for j in range(i, length):
            if targets[i] + targets[j] == target:
                return targets[i], targets[j]


def find_dst_value2(target: int, targets: list):
    """
    time complexity O(N) + O(N*logN)
    :param target:
    :param targets:
    :return:
    """
    targets.sort()
    i, j = 0, len(targets)-1
    while i < j:
        left_value = targets[i]
        right_value = targets[j]
        if left_value + right_value == target:
            return left_value, right_value
        if left_value + right_value > target:
            j -= 1
        elif left_value + right_value < target:
            i += 1


# test
lst = [1, 5, 2, 7, 4, 9]
t3 = 7
print(find_dst_value2(t3, lst))

