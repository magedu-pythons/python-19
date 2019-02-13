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
