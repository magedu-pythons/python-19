#1.判断一个5位数是不是回文数
def is_palin(num):
    s = str(num)
    length = len(s)
    for i in range( length//2 ):
        if s[i] != s[-i-1]:
            print('{} is not palindromic number'.format(num))
            return False
    print('{} is palindromic number'.format(num))
    return True
        
#test 
num = 12321
is_palin(num)

num = 12322
is_palin(num)


#-------------------------------------------------------------------
print('-------------------------------------------------------------------')

#2.随机生成20个数, 并且筛选出其中最大的3个数
#思路:three为结果列表,每生成一个数就将three中,小于这个数字的元素替换为这个数字
import random

lst = []
three = []

def change(three:list, item:int): #如果item比three中的任意一个数大,就用item替换three中的内容
    for i,n in enumerate(three):
        if item > n:
            three[i] = item
            break
    
for i in range(20):
    one = random.randint(0,100)
    lst.append(one)
    if i <= 2:
        three.append(one)
    else:
        change(three,one)

#result
print('随机生成20个数:{}'.format(lst))
print('其中最大的三个数为:{}'.format(three))




"""
(0 + 0)

    good!
"""

