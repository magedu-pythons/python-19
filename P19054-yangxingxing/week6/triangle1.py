# 1, 第几行的第几个元素。 简单写法
import datetime
line = 1000
num = 567

if num == 1 or num == line:
    print(1)
elif num == 2 or num == line - 1:
    print(line-1)
else:
    start = datetime.datetime.now()
    list1 = [[1], [1, 1]]
    for i in range(2, line - 1):
        list1.append([1] * (i + 1))
        middle = i // 2
        for y in range(1, middle + 1):
            list1[i][y] = list1[i - 1][y - 1] + list1[i - 1][y]
            list1[i][-(y + 1)] = list1[i][y]

    list1.append([1] * line)
    #    if num > line // 2:
    #        point = (line - num)
    #    else:
    #        point = num - 1
    #    list1[line-1][point] = list1[line-2][point-1] + list1[line-2][point]
    #    list1[line-1][-(point+1)] = list1[line-1][point]

    list1[line - 1][num - 1] = list1[line - 2][num - 2] + list1[line - 2][num - 1]
    end = datetime.datetime.now()

    print(list1[line - 1][num - 1])
    print((end-start).total_seconds())


# 2, 优化写法，使用组合数公式.    m!/n!(m-n)!
#  m 等于 行减1，   n等于第几个元素减1.
#  m! 表示m的阶乘。
#line = 7
#num = 3
if num == 0 or num == line:
    print(1)
elif num == 1 or num == line - 1:
    print(line-1)
else:
    start = datetime.datetime.now()
    m = line - 1
    n = num - 1
    target = [1]
    for i in range(2, m+1):
        target[0] *= i
        if i == n:
            target.append(target[0])
        if i == m - n:
            target.append(target[0])
    point_num = target[0] // (target[1] * target[2])
    end = datetime.datetime.now()
    print(point_num)
    print((end-start).total_seconds())













