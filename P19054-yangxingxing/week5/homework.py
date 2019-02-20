# 1、 5位数，判断是否是回文数
num = 12321

num_list = list(str(num))
if num_list[0:2] == num_list[:2:-1]:
    print('{} 是回文数'.format(num))
else:
    print('{} 不是回文数'.format(num))

# 2、 随机生成20个数字， 筛选出最大的3个数.
import random
limit = 20
num_list = [0] * limit
for i in range(limit):
    num_list[i] = random.randint(1, 100)

for y in range(3):
    for n in range(limit - y - 1):
        if num_list[n] > num_list[n+1]:
            num_list[n], num_list[n+1] = num_list[n+1], num_list[n]

print(num_list[-3:])



"""
(0 + 0)

    题1 使用更通用的实现，比如6位数 或者 7位数等
    题2 参考答案的简易实现
"""