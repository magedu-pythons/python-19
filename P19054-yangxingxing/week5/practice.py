# 1、冒泡
import random, datetime

start = datetime.datetime.now()
list_length = 10000
list1 = [1] * list_length
for i in range(list_length):
    list1[i] = random.randrange(0, 100000)

for i in range(len(list1)-1, 0, -1):
    for y in range(i):
        if list1[y] < list1[y+1]:
            list1[y], list1[y+1] = list1[y+1], list1[y]

end = datetime.datetime.now()
print((end-start).total_seconds())
print(list1)
print(sorted(list1, reverse=True) == list1)





