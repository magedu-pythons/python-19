# 2、实现一个函数，输入字符串，判断该字符串是否不含有重复字符


def find_repeat(s: str):
    lst = []
    for i in s:
        if i in lst:
            return 'repeat'
        lst.append(i)


print(find_repeat('aew21'))