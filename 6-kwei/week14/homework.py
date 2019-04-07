# 1、实现一个可迭代的类
class IterClass:
    def __init__(self, *args):
        self.body = args

    def __iter__(self):
        return iter(self.body)

    def p(self):
        for item in self.body:
            print(item)


# test
i = IterClass([1, 2, 3], [4, 5, 6], [7, 8], [9])
for it in i:
    print(it)


# 2、给出一个无序的整型列表，找出最长连续元素序列的长度，时间复杂度要求在线性时间内。
# 例如：
# 输入：[8,1,9,3,2,4]，那么其最长连续序列是[1,2,3,4]，即输出长度为4
def find_longest_squece2(src):
    max_count = 0
    src = set(src)
    for i in src:
        if i - 1 not in src:
            num = i + 1
            while True:
                num += 1
                if num not in src:
                    break
            max_count = max(max_count, num - i)
    return max_count


# test
print('最长子串的长度:', find_longest_squece2([8, 1, 9, 3, 2, 4]))


# 3、输入一个字符串，求不含有重复字母的最长子串的长度
# 例如：
# 输入字符串'aaa'，其不含有重复字母的最长子串为‘a’，输出长度为1
def lengthoflongestsubstring(s):
    max_len = 0  # 存储历史循环中最长的子串长度
    if s is None or len(s) == 0:  # 判断传入的字符串是否为空
        return max_len
    str_dict = {}  # 定义一个字典，存储不重复的字符和字符所在的下标
    one_max = 0  # 存储每次循环中最长的子串长度
    start = 0  # 记录最近重复字符所在的位置+1
    for i in range(len(s)):
        # 判断当前字符是否在字典中和当前字符的下标是否大于等于最近重复字符的所在位置
        if s[i] in str_dict and str_dict[s[i]] >= start:
            start = str_dict[s[i]] + 1  # 记录当前字符的值+1
        one_max = i - start + 1  # 在此次循环中，最大的不重复子串的长度
        str_dict[s[i]] = i  # 把当前位置覆盖字典中的位置
        max_len = max(max_len, one_max)   # 比较此次循环的最大不重复子串长度和历史循环最大不重复子串长度
    return max_len




"""
(0 + 0)

    第一题参考答案
"""