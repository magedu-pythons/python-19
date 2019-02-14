#!/usr/bin/env python
#
# 1.1 杨辉三角
myLine = 21
myList = [[1], [1, 1]]
for i in range(2, myLine):
    newList = [1] * (i + 1)
    for y in range(1, i):
        newList[y] = myList[i-1][y-1] + myList[i-1][y]
    myList.append(newList)
print(myList)

# 1.2 对称计算
myLine = 21
myList = [[1], [1, 1]]
for line in range(2, myLine):
    newList = [1] * (line + 1)
    for index in range(1, line//2+1):
        newList[index] = myList[line-1][index-1] + myList[line-1][index]
        newList[-(index+1)] = newList[index]
    myList.append(newList)
print(myList)


# 1.3 去掉里面的newList列表。
myLine = 21
myList = [[1], [1, 1]]
for line in range(2, myLine):
    myList.append([1] * (line + 1))
    for index in range(1, line//2+1):
        myList[line][index] = myList[line-1][index-1] + myList[line-1][index]
        myList[line][-(index+1)] = myList[line][index]
print(myList)
