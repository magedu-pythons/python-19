# 应该是个闭包问题 。。。再想想





# 判断字符串是否有重复
def func(str1):
    set1=set(str1)
    if len(set1) < len(str1):
        print("{}有重复".format(str1))
    else:
        print("{}没有重复".format(str1))

func('abcdef')

func('abbcd')




"""
(0 + 0)

    参考答案的解法
"""