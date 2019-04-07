# 1、实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出 现的地址；否则，返回None。


def substring(str1, str2):
    return str1.index(str2) if str2 in str1 else None


print(substring('xyz', 'xy'))

# 2、给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
# 如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11


def judge(array: list, num: int):
    for i in array:
        if num - i in array:
            return num-i, i
    else:
        return None


lst = [1, 5, 2, 7, 4, 9]
print(judge(lst, 11))





"""
(0 + 0)

    第二题参考答案的解法
"""