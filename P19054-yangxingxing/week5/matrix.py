line = input('Enter your line:> ').strip()
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


