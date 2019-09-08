# 2、
# 给一个目标数 target, 一个非负整数 k, 一个按照升序排列的数组 A。
# 在 A 中找与 target 最接近的 k 个整数。
# 返回这 k 个数并按照与 target 的接近程度从小到大排序，如果接近程度相当，那么小的数排在前面。
# 例如：
# Given A = [1, 2, 3], target = 2 and k = 3, return [2, 1, 3].
# Given A = [1, 4, 6, 8], target = 3 and k = 3, return [4, 1, 6].


def k_closest_numbers(array, target, k):
    length = len(array)

    left, right = find_position(array, target)
    result = []
    while k > 0 and (left >= 0 or right < length):
        if left >= 0 and right < length:
            if abs(array[left] - target) <= abs(array[right] - target):
                result.append(array[left])
                left -= 1
            else:
                result.append(array[right])
                right += 1
        elif right == length:
            result.append(array[left])
            left -= 1
        else:
            result.append(array[right])
            right += 1
        k -= 1
    return result


def find_position(array, target):
    length = len(array)
    left, right = 0, length - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if array[mid] > target:
            right = mid
        else:
            left = mid
    return left, right

print(k_closest_numbers([3,2,5,6,1], 3, 2))