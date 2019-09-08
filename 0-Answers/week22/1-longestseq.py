# 1、给出一个无序的整型列表，找出其最长连续元素序列的长度，时间复杂度要求在线性时间内。
#   举例： 输入[8,1,9,3,2,4]，那么其最长的连续序列是[1,2,3,4]，即输出长度为4


def find_longest_consequence(num):
    d = {}

    for x in num:
        d[x] = 1

    ans = 0

    for x in num:
        if x in d:
            length = 1
            del d[x]
            l = x - 1
            r = x + 1
            while l in d:
                del d[l]
                l -= 1
                length += 1
            while r in d:
                del d[r]
                r += 1
                length += 1
            if ans < length:
                ans = length

    return ans


print(find_longest_consequence([8, 5, 1, 9, 3, 2, 4]))