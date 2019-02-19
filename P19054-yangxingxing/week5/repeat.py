import random

# 重复的数字
# 这种方式跟列表索引关联，所以不能处理很大的数字和小数
#limit = 10
#list1 = [0] * limit
#for i in range(limit):
#    list1[i] = random.randint(1, 20)
#status = [0] * 21
#for i in list1:
#    status[i] += 1
#
#for y in range(len(status)):
#    if status[y] > 1:
#        print('{} 是重复的, 次数: {}'.format(y, status[y]))
#    elif status[y]:
#        print('{} 不是重复的'.format(y))

# 以其它列表做对应的方式
limit = 100
list1 = [0] * limit
repeat = []
count = []
not_repeat = []
status = [1] * limit
for i in range(limit):
    list1[i] = random.randint(1, 20)

for x in range(limit):
    if status[x] > 1:
        continue
    for y in range(x+1, limit):
        if status[y] > 1:
            continue
        if list1[x] == list1[y]:
            status[x] += 1
            status[y] += 1
    else:
        if status[x] > 1:
            repeat.append(list1[x])
            count.append(status[x])
        else:
            not_repeat.append(list1[x])

#print(list1)
print(list(zip(repeat, count)))
print(not_repeat)
#print(status)





