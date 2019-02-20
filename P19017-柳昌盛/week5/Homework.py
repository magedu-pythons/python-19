# 1判断回文数
num = '12321'     # str(input("请输入数字:"))
flag = False
for i in range(len(num)//2):
    if num[i] == num[-1-i]:
        flag = True
    else:
        flag = False
print("是回文数") if flag else print("不是回文数")

# 2求20个数中的最大的三个数
import random
random_list = []
max_num = []
for i in range(20):
    random_list.append(random.randint(1, 100))
for i in range(3):
    a = max(random_list)
    max_num.append(a)
    random_list.remove(a)
print(max_num)



"""
(0 + 0)

    good
"""