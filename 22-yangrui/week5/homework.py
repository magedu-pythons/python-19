#1、问题描述：一个5位数，判断它是不是回文数。
n=input(">>>")
num=str(n)
length=len(num)
for i in range(length//2):
    if num[i]!=num[length-1-i]:
        print("This is not palindrome number")
        break
else:
    print("This is palindrome number")

#2、随机生成20个数字，并且筛选出其中最大的3个数
#方法1：
import random
lst=[]
for i in range(20):
    lst.append(random.randint(1,1000))
print(lst)
lst.sort(reverse=True)
print(lst[:3])

#方法2：
import random
lst=[]
for i in range(20):
    lst.append(random.randint(1,1000))
print(lst)
for i in range(3):
    the_max=max(lst)
    print(the_max)
    lst.remove(the_max)