��һ�⣺local��global��shell3�ַ�ʽ����
��local��global��shellӰ��python�汾�ĵ�������global���������Ӱ��ȫ�֣�
localֻӰ�����õĵ�ǰ����Ŀ¼�Լ�����Ŀ¼��shellֻӰ�쵱ǰ�Ự


�ڶ��⣺��ӡ쳲���������
����һ��
f0 = 0 
f1 = 1
n = int(input("�����������쳲��������У�"))
print("��һ�����ǣ�",f0��f1)
for i in range(2,n):
    fn = f0 + f1
    f0 = f1
    f1 = fn
    print(fn)
��������
f0 = 0 
f1 = 1
count = 2
n = int(input("�����������쳲��������У�"))
print("��һ������:",f0,f1)
while True:
    fn = f0 + f1
    count+=1
    print(fn)
    f0 = f1 
    f1 = fn
    if count>n-1:
        break


�����⣺ʹ�� Python ʵ��������� 200�����ظ������루�����Ż�ȯ�����ַ������ȴ���5����
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
#���������1/36**5�ظ��Ŀ����ԣ�ȥ�صĻ���û���뵽�÷���




"""
(0 + 0)

    有语法错误，请使用pycharm写代码
"""

