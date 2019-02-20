line = input('Enter your line:> ').strip()
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

