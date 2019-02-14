# coding=utf-8
#题1、问题描述：一个5位数，判断它是不是回文数。
import math
num=input('please input a number with length 5:').strip()  #TODO 非五位数的问题，以及while循环输入的问题
def pali_num(num):
    print('what you input number is:{}'.format(num))
    length=len(num)
    flag=True
    for i in range(math.ceil(length//2)):
        if num[i]!=num[-i-1]:
            # print('pali_num :NO')
            flag=False
    if flag:
        print('pali_num :YES')
    else:
        print('pali_num :NOPE')
pali_num(num)

#题2、随机生成20个数字，并且筛选出其中最大的3个数
#需要通过排序来解决，然后选择排序每一轮就能找到最大值，找三轮选择排序就好
import random
num_lst=[random.randint(1,100) for i in range(20)]
print(num_lst)
def choosesort(num_lst): #TODO 有可能存在第2到4名都是相同的数值
    maxindex=0
    newlst=[]
    for i in range(3):
        num=len(num_lst)-i
        for j in range(num):
            if num_lst[j]>num_lst[maxindex]:
                maxindex=j
        newlst.append(num_lst[maxindex])
    return newlst
print(choosesort(num_lst))



"""
(0 + 0)

    第二题参考答案的更简易实现
"""

