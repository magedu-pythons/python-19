#2、打印出100以内的斐波那契数列，使用2种方法实现
#方法1
pre=1
print(pre)
sec=1
while sec<100:
    pre,sec=sec,pre+sec
    print(pre)
    
#方法2
lst=[0]*20
tmp=1
for i in range(len(lst)):
    if i<=1:
        lst[i]=1
    else:
        tmp,lst[i]=lst[i-1],lst[i-1]+tmp
        if lst[i]>100:
            break
print(lst[:i])


#3、使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上
import random
for i in range(200):
    num=random.randrange(100000,10000000)
    print(num)