
#No.1
a=1
b=1
while b<100: 
    print(b)
    a,b=b,a+b 

#No.2

def fib_seq(n): 
    if n==1: 
        return 1 
    elif n==2: 
        return 1 
    else: 
        return fib_seq(n-1)+fib_seq(n-2) 

for i in range(1,100): 
    num=fib_seq(i)
    if num>=100: 
        break 
    print(num) 

#3
import random
for i in range(0,200):
    print(random.randint(100000,1000000))




"""
(0 + 0)

    参考答案实现
"""