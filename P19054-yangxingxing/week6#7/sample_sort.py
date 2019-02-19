import random

# 简单选择排序
limit = 10
list1 = [0] * limit
for i in range(limit):
    list1[i] = random.randint(1, 50)

print(list1)
for i in range(limit-1):
    maxindex = i
    for y in range(i+1, limit):
        if list1[y] > list1[maxindex]:
            maxindex = y
    if i != maxindex:
        list1[i], list1[maxindex] = list1[maxindex], list1[i]
print(list1)


# 简单二元选择排序
limit = 9
list1 = [0] * limit
for i in range(limit):
    list1[i] = random.randint(1, 50)
print(list1)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#list1 = [3, 4, 4, 4, 4, 3, 4, 4, 4]
for i in range(limit // 2):
    maxindex = i
    #    minindex = -i - 1
    minindex = i
    for y in range(i+1, limit-i):
        if list1[y] > list1[maxindex]:
            maxindex = y
        if list1[y] < list1[minindex]:
            minindex = y
    if maxindex == minindex:
        break
    if i != maxindex:
        list1[i], list1[maxindex] = list1[maxindex], list1[i]
        if minindex == i:
            minindex = maxindex
    if -i-1 != minindex:
        list1[-i-1], list1[minindex] = list1[minindex], list1[-i-1]
print(list1)

