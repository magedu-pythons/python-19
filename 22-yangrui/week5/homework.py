#1������������һ��5λ�����ж����ǲ��ǻ�������
n=input(">>>")
num=str(n)
length=len(num)
for i in range(length//2):
    if num[i]!=num[length-1-i]:
        print("This is not palindrome number")
        break
else:
    print("This is palindrome number")

#2���������20�����֣�����ɸѡ����������3����
#����1��
import random
lst=[]
for i in range(20):
    lst.append(random.randint(1,1000))
print(lst)
lst.sort(reverse=True)
print(lst[:3])

#����2��
import random
lst=[]
for i in range(20):
    lst.append(random.randint(1,1000))
print(lst)
for i in range(3):
    the_max=max(lst)
    print(the_max)
    lst.remove(the_max)