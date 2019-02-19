#
import random
list1 = [0] * 1000
for i in range(1000):
    list1[i] = random.randint(0,10000)

def test1(list1):
    for i in range(len(list1)-1, 0, -1):
        for y in range(i):
            if list1[y] < list1[y+1]:
                list1[y], list1[y+1] = list1[y+1], list1[y]
    return list1

test1(list1)
print(list1 == sorted(list1, reverse=True))

#

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


# 上面两种是一样的， 只是为了练习.
# 1、冒泡, 在缺乏特定条件的随机序列，速度没有前面两种快。
import random, datetime

start = datetime.datetime.now()
list_length = 10000
list1 = [1] * list_length
for i in range(list_length):
    list1[i] = random.randrange(0, 100000)

for i in range(len(list1)-1, 0, -1):
    flag = True
    for y in range(i):
        if list1[y] > list1[y+1]:
            flag = False
            list1[y], list1[y+1] = list1[y+1], list1[y]
    if flag:
        break

end = datetime.datetime.now()
print((end-start).total_seconds())
print(list1)
print(sorted(list1) == list1)




