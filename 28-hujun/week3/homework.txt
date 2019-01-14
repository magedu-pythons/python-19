第一题：local、global、shell3种方式区别
答：local、global、shell影响python版本的的作用域，global作用域最大，影响全局；
local只影响设置的当前工作目录以及其子目录；shell只影响当前会话


第二题：打印斐波那契数列
方法一：
f0 = 0 
f1 = 1
n = int(input("你想求多少项斐波那契数列："))
print("第一二项是：",f0，f1)
for i in range(2,n):
    fn = f0 + f1
    f0 = f1
    f1 = fn
    print(fn)
方法二：
f0 = 0 
f1 = 1
count = 2
n = int(input("你想求多少项斐波那契数列："))
print("第一二项是:",f0,f1)
while True:
    fn = f0 + f1
    count+=1
    print(fn)
    f0 = f1 
    f1 = fn
    if count>n-1:
        break


第三题：使用 Python 实现随机生成 200个无重复激活码（或者优惠券），字符串长度大于5以上
import random
count = 0
for i in range(200):
    m = ""
    for j in range(5):
        n = random.choice('abcdefghijklmnopqrstuvwxyz0123456789')
        m = m + n
    count+=1
    print(m)
print(count)
#这里可能有1/36**5重复的可能性，去重的话，没有想到好方法