def sorted1(iterable, reverse=False, key=None):
    list2 = []
    for i in iterable:
        for x, y in enumerate(list2):
            ii = key(i) if key else i
            yy = key(y) if key else y
            flag = ii < yy if not reverse else ii > yy
            if flag:
                list2.insert(x, i)
                break
        else:
            list2.append(i)
            continue

    return list2



dd = [1, 2, 7, 4, 2, 1, 0, 8]
print(sorted1(dd, key=lambda x: 200 if x==4 else x))