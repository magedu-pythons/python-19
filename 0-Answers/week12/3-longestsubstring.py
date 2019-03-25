# 3、输入一个字符串，求不含有重复字母的最长子串的长度
# 例如：
#    输入字符串'aaa'，其不含有重复字母的最长子串为‘a’，输出长度为1

def longest_substring_length(s: str):
    length = len(s)
    start = 0
    max_len = 0
    d = {}
    for i in range(length):
        k = s[i]
        if k in d and d.get(k) >= start:
            start = d.get(k) + 1
        d[k] = i
        max_len = max(max_len, i - start + 1)

    return max_len


# test
print('Q3:', 80 * '-')
print(longest_substring_length('aaaabbcdefusqq'))