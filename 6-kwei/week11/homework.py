# 1、请实现函数 new_counter ，使得调用结果如下：
#       c1 = new_counter(10)
#       c2 = new_counter(20)
#       print（c1(), c2(), c1(), c2()）
#       outputs ：
#       11 21 12 22
def new_counter(num:int):
    def _wrapper():
        nonlocal num
        num += 1
        return num
    return _wrapper

c1 = new_counter(10)
c2 = new_counter(20)

#test
print(c1(),c2(),c1(),c2())

# 2、实现一个函数，输入字符串，判断该字符串是否不含有重复字符 
def if_repeat(string:str): #一个字符串中有重复就返回True, 没有重复就返回False
    temp = dict() 
    for c in string:
        temp[c] = temp.get(c,0) + 1
        #print(temp)
        if temp[c] > 1:
            return True
    return False

#test 
print(if_repeat('aa'))
print(if_repeat('qwertyuaa'))
print(if_repeat('asdfghjkl'))