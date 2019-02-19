

print('1、问题描述：一个5位数，判断它是不是回文数。')

a = int(input('请输入一个五位数：'))
lst = [i for i in str(a) ]
if len(lst) ==5:
    if lst[0] == lst[4] and lst[1] == lst[3]:
        print("输入的数字是回文数")
    else:
        print("输入的数字不是回文数")
else:
    print('数字不是五位数')



print('======================================================')

print('2、随机生成20个数字，并且筛选出其中最大的3个数')
import random as rd
lst1 = [rd.randint(0,100) for j in range(0,20)]
print(lst1)

lst2 = [lst1.pop(lst1.index(max(lst1))) for j in range(3)]
print('最大的三个数字分别为：',lst2)
    



