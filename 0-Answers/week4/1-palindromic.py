# 1、问题描述：一个5位数，判断它是不是回文数。


def is_palindromic(num: int):
    s1 = str(num)
    s2 = s1[::-1]
    # reversed  abc->cba  aba -> aba
    if s1 == s2:
        return '{} 是回文数'.format(num)
    return '{} 不是回文数'.format(num)


def is_palindromic_2(num: int):
    s1 = str(num)
    length = len(s1)
    # 12331
    for i in range(length // 2):
        if s1[i] != s1[length - i - 1]:
            return '{} 不是回文数'.format(num)
    return '{} 是回文数'.format(num)