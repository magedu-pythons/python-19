#1、实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出现的地址；否则，返回None。
def func(str1:str,str2:str):
    if str1.find(str2) == -1:
        return 'None'
    return str1.find(str2)

s1 = 'abcg432'
s2 = '43'
print(func(s1,s2))

#output: 4
s1 = 'abcg432'
s2 ='cb'
print(func(s1,s2))
#output 'None'



# 2、给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
# 如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11
num = int(input('please input number>>'))
lst =[1,5,2,7,4,9]
n = len(lst)
for i in range(n):
    for j in range(i+1,n):
        if lst[i] + lst[j] == num :
            print("success found two number:{} {}".format(lst[i],lst[j]))

# please input number>>11
# success found two number:2 9
# success found two number:7 4




"""
(0 + 0)

    第二题参考答案更快实现
"""