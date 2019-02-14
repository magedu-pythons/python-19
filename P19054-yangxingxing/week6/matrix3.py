line = input('Enter your line:> ').strip()
list1 = [line.split()]
sep = len(list1[0])
count = 1
while True:
    line = input('Enter your line:> ').strip()
    if not line:
        break
    count += 1
    list1.append(line.split())

if count == sep:
    for x in range(sep):
        for y in range(x, count):
            if y == x:
                continue
            list1[x][y], list1[y][x] = list1[y][x], list1[x][y]
elif count > sep:
    for x in range(sep):
        for y in range(x, count):
            if y == x:
                continue
            elif y < sep:
                list1[x][y], list1[y][x] = list1[y][x], list1[x][y]
            else:
                list1[x].append(list1[y].pop(0))
    list1 = list1[:sep]
elif count < sep:
    for x in range(count):
        for y in range(x, sep):
            if y == x:
                continue
            elif y < count:
                list1[x][y], list1[y][x] = list1[y][x], list1[x][y]
            else:
                if x:
                    list1[y].append(list1[x].pop(count))
                else:
                    list1.append([list1[x].pop(count)])

print(list1)




