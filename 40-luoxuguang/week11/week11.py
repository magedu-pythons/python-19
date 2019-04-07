#1、请实现函数 new_counter ，使得调用结果如下：
#  c1 = new_counter(10)
#  c2 = new_counter(20)
#  print（c1(), c2(), c1(), c2()）
#  outputs ：11 21 12 22

def new_counter(num):
    def inc(step = 1):
        nonlocal num
        num += 1
        return num
    return inc

c1 = new_counter(10)
c2 = new_counter(20)
print(c1(),c2(),c1(),c2())

#2、实现一个函数，输入字符串，判断该字符串是否不含有重复字符
#利用集合可以去重的特性，把字符串变成集合，长度相等则不含重复，不等则含重复字符

def repeat(s):
    col =set()
    l =len(s)
    for i in range(l):
        col.add(s[i])
    print('{}'.format("repeat string:" if len(col)!=l else "not repeat"))

while True:
    s =input('>>>')   #回车结束判断
    if s == '':
        print("结束判断")
        break
    repeat(s)

#测试>>>abcde
# not repeat
# >>>abbef
# repeat string:
# >>>
# 结束判断




"""
(0 + 0)

    good!
"""