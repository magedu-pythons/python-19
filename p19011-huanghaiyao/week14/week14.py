#第一题
class iterable:
    def __iter__(self):
        count = 0
        while count < 100:
            yield count
            count += 1


#第二题
def max_succession(lst):
    lst.sort()
    print(lst)
    if lst:
        start = lst[0]  #设置列表中的第一个数为开始比较的量
    else:
        print('This list in empty')
        return

    max_c = 1   #默认最大连续长度为1
    count = 0   #记录连续个数的变量
    for x in lst:
        if x == start:
            count += 1  #更新最大连续数
            start += 1  #步进1，更新比较条件
        else:
            max_c = max_c if max_c > count else count   #记录最大的连续个数
            count = 1   #重置
            start = x + 1   #重置

    return max_c

#第三题
def max_succession2(string):
    s = set()
    max_c = 1 if string else 0  #非空字符串默认最大连续长度为1
    for ch in string:
        if ch not in s:
            s.add(ch)
        else:
            max_c = max_c if max_c > len(s) else len(s)
            s.clear()   #重置集合
            s.add(ch)   #将运行时当前字符记为第一个不同的字符
    else:
        max_c = max_c if max_c > len(s) else len(s)     #这一句是解决两种情况
    return max_c                                        #一，全字符串都是不同的，导致for语句中的max_c得不到更新
                                                        #二，最后一串不同的字符串，进不了else子句max_c得不到更新
