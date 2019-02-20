import datetime, time
def test1(limit):
    list1 = [2,3]
    for i in range(5,limit,2):
        for y in range(3,int(i**0.5)+1,2):
            if i % y == 0:
                break
        else:
            list1.append(i)
    return list1

def test2(limit):
    list1 = [2,3]
    for i in range(5,limit,2):
        tmp = i ** 0.5
        for y in list1:
            if i % y == 0:
                break
            if y > tmp:
                list1.append(i)
                break
    return list1

start = datetime.datetime.now()
list1 = test1(10000000)
end = datetime.datetime.now()
print('time: {} s'.format((end-start).total_seconds()))
print(len(list1))

time.sleep(2)
start = datetime.datetime.now()
list1 = test2(10000000)
end = datetime.datetime.now()
print('time: {} s'.format((end-start).total_seconds()))
print(len(list1))
