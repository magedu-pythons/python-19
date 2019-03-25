# 以新列表的方式存储矩阵，简单通用， 方阵矩阵都可以。

import datetime
#list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#list1 = [[1, 2], [3, 4], [5, 6], [7, 8]]
#list1 = [[1, 2, 3, 4], [5, 6, 7, 8]]
list1 = [[1,2,3] * 1000, [4,5,6] * 1000] * 3000

# 1、 append 的方式
start = datetime.datetime.now()
tmp_list = []
for xkey, xvalue in enumerate(list1):
    for ykey, yvalue in enumerate(xvalue):
        if len(tmp_list) <= ykey:
            tmp_list.append([])
        tmp_list[ykey].append(yvalue)
end = datetime.datetime.now()
print((end-start).total_seconds())
#print(tmp_list)


# 2、 预创建列表的方式
start = datetime.datetime.now()
tmp_list = [[0 for _ in range(len(list1))] for _ in range(len(list1[0]))]
for xkey, xvalue in enumerate(list1):
    for ykey, yvalue in enumerate(xvalue):
        tmp_list[ykey][xkey] = yvalue
end = datetime.datetime.now()
print((end-start).total_seconds())
#print(tmp_list)


# 3、 不使用enumerate的方式.
start = datetime.datetime.now()
tmp_list = [[0 for _ in range(len(list1))] for _ in range(len(list1[0]))]
for x in range(len(list1)):
    for y in range(len(list1[0])):
        tmp_list[y][x] = list1[x][y]
end = datetime.datetime.now()
print((end-start).total_seconds())
#print(tmp_list)


# 4、 上面都是先把x轴放入y轴， 如把list1[0][0]  [0][1]  [0][2]  分别放入新列表的[0][0] [1][0] [2][0]
#     把原列表第一个列表中的内容，依次放入新列表中的第一个第二第三...列表。
#     下面把y轴放入x轴,  把list1[0][0] [1][0] [2][0]  放入新列表的第一个列表.
start = datetime.datetime.now()
tmp_list = [[0 for _ in range(len(list1))] for _ in range(len(list1[0]))]
for y in range(len(list1[0])):
    for x in range(len(list1)):
        tmp_list[y][x] = list1[x][y]
end = datetime.datetime.now()
print((end-start).total_seconds())
#print(tmp_list)

# 第4种速度最快， 在列表中顺序写比顺序读快。  1，2，3  都是从列表中拿出数据，然后依次第一二三.... 列表，
# 第4种是从第一二三.....列表中拿出来数据，依次写入同一个列表。
# 有时候第二种比这一种快。


