# 矩阵， 下面这三种只是打印成了矩阵图形， 并没有在列表中形成结构。

line = input('Enter your line:> ').strip()
#  以range步长打印的。
list1 = line.split()
sep = len(list1)
while True:
    line = input('Enter your line:> ').strip()
    if not line:
        break
    list1.extend(line.split())

for i in range(sep):
    for y in range(i, len(list1), sep):
        print(list1[y], end='\t')
    print()


# 以列表切片打印的
#line = input('Enter your line:> ').strip()
list1 = line.split()
sep = len(list1)
while True:
    line = input('Enter your line:> ').strip()
    if not line:
        break
    list1.extend(line.split())

for i in range(sep):
    data = list1[i::sep]
    print(*data, sep='\t')


# 也是以切片，只是打印了原来的图形和改变以后的图形
#line = input('Enter your line:> ').strip()
list1 = line.split()
sep = len(list1)
count = 1
while True:
    line = input('Enter your line:> ').strip()
    if not line:
        break
    count += 1
    list1.extend(line.split())

middle = sep // 2
for i in range(sep):
    format_str = '{:>3}' * sep
    format_str += '{:^10}'
    format_str += '{:<3}' * count

    data = list1[i*sep:sep*(i+1)] or [' '] * sep
    if i == middle:
        data.append('<<==>>')
    else:
        data.append(' ' * 6)
    data.extend(list1[i::sep])
    print(format_str.format(*data))
