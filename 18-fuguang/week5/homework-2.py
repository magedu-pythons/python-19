import random
lst = []

for i in range(20):
    num = random.randint(0,1000)
    lst.append(num)

lst.sort()
lst.reverse()
print(lst[:3])