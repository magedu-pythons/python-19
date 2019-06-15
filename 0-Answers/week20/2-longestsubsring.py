# 2、输入一个字符串，求不含有重复字母的最长子串长度
# 举例：输入字符串 'aaaa'，其不含有重复字母的最长子串为‘a’，输出长度为1



def length_of_longest_substring(s):
    unique_chars = set()
    j = 0
    n = len(s)
    longest = 0
    for i in range(n):
        while j < n and s[j] not in unique_chars:
            unique_chars.add(s[j])
            j += 1
        longest = max(longest, j - i)
        unique_chars.remove(s[i])

    return longest

print(length_of_longest_substring('aaa'))