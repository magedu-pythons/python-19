#请实现函数 new_counter ，使得调用结果如下：
      # c1 = new_counter(10)
      # c2 = new_counter(20)
      # print（c1(), c2(), c1(), c2()）
      # outputs ：
      # 11 21 12 22


def new_counter(param):
    param = param
    def wrapper():
        nonlocal param
        param += 1
        return param
    return wrapper


#实现一个函数，输入字符串，判断该字符串是否不含有重复字符

from collections import Counter
st1 = 'asdfgh'
st2 = 'hello'

def check(st):
    for v in Counter(st).values():
        if v > 1:
            return 'repetition'
    return 'No repetition'




"""
(0 + 0)

    尽量不要用自带的模块解决，自行实现
"""