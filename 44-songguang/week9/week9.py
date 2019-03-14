# 1 判断子串
def fn(str1: str, str2: str):
    """判断字符串2是否为字符串1的子串"""
    if len(str2) > len(str1):
        print('None')
        return
    for index, i in enumerate(str1[:len(str1) - len(str2) + 1]):
        if i == str2[0]:
            if str1[index:index + len(str2)] == str2:
                print(index)
                return
    print('None')


fn('aacccvsabc', 'abc')


#2、给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11

lst =[1,5,2,7,4,9]

def func(lst:list,n):
    for index,i in enumerate(lst) :
        if i < n:
            for j in lst[index+1:]:
                if i + j == n:
                    print(i,j )
                    return
    print("None")
    return

func(lst,11)
