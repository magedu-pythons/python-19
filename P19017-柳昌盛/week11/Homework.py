# 1、请实现函数 new_counter ，使得调用结果如下：
#       c1 = new_counter(10)
#       c2 = new_counter(20)
#       print（c1(), c2(), c1(), c2()）
#       outputs ：
#       11 21 12 22


def new_counter(num):
    def _new_counter():
        nonlocal num
        num += 1
        return num
    return _new_counter


c1 = new_counter(10)
c2 = new_counter(20)
print(c1(), c2(), c1(), c2())
# 2、实现一个函数，输入字符串，判断该字符串是否不含有重复字符


def judge_repeated(string: str):
    if len(set(string.strip())) == len(string):
        return "{}中没有重复的字符".format(string)
    str_dict = {}
    for s in string:
        str_dict[s] = str_dict.get(s, 0) + 1
    return sorted(str_dict.items(), key=lambda item: item[1], reverse=True)


ss = "abcde"
print(judge_repeated(ss))



"""
(0 + 0)

    goood
"""