import random
limit = 10
list1 = [0] * limit
for i in range(limit):
    list1[i] = random.randint(1,20)
status = [0] * 21
for i in list1:
    status[i] += 1

for y in range(len(status)):
    if status[y] > 1:
        print('{} 是重复的, 次数: {}'.format(y, status[y]))
    elif status[y]:
        print('{} 不是重复的'.format(y))

