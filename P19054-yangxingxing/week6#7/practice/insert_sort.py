import random
limit = 8
#list1 = [random.randint(1, 100) for i in range(limit)]
list1 = [50, 12, 27, 86, 69, 63, 45, 28]
list1[:0] = [0]
print(list1)
print('--------')

for i in range(2, limit+1):
    list1[0] = list1[i]
    if list1[i-1] > list1[0]:
        for n in range(i-1, 0, -1):
            if list1[n] > list1[0]:
                list1[n+1] = list1[n]
            else:
                list1[n+1] = list1[0]
                break
        else:
            list1[n] = list1[0]
print(list1)


