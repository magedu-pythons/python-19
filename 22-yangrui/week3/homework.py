#2����ӡ��100���ڵ�쳲��������У�ʹ��2�ַ���ʵ��
#����1
pre=1
print(pre)
sec=1
while sec<100:
    pre,sec=sec,pre+sec
    print(pre)
    
#����2
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


#3��ʹ�� Python ʵ��������� 200 ���ظ������루�����Ż�ȯ�����ַ������ȴ���5����
import random
for i in range(200):
    num=random.randrange(100000,10000000)
    print(num)