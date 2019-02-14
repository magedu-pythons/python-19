
list1 = [[1], [1, 1]]

for i in range(2, 100):
    list1.append([1] * (i + 1))
    middle = i // 2
    for y in range(1, middle+1):
        list1[i][y] = list1[i-1][y-1] + list1[i-1][y]
        list1[i][-(y+1)] = list1[i][y]
print(list1)



