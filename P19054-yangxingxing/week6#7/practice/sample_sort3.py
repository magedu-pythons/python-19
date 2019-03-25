# 重复练习
import random
limit = 30
list1 = [0] * limit
for i in range(limit):
    list1[i] = random.randint(1, 50)
print(list1)
print()

# 简单选择排序
#for i in range(limit-1):
#    max_index = i
#    for y in range(i+1, limit):
#        if list1[y] > list1[max_index]:
#            max_index = y
#    if max_index != i:
#        list1[i], list1[max_index] = list1[max_index], list1[i]
#print(list1)

# 简单二元选择排序
for i in range(limit // 2):
    max_index = i
    min_index = i
    for y in range(i+1, limit-i):
        if list1[y] > list1[max_index]:
            max_index = y
        elif list1[y] < list1[min_index]:
            min_index = y
    if min_index == max_index:
        break
    if max_index != i:
        list1[i], list1[max_index] = list1[max_index], list1[i]
        if min_index == i:
            min_index = max_index
    if min_index != -i-1:
        list1[-i-1], list1[min_index] = list1[min_index], list1[-i-1]
    print(list1)

print()
print(list1)

