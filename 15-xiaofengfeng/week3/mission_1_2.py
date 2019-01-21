#打印出100以内的斐波那契数列，使用2种方法实现
first = 1
second = 1
print("The number :", first)
print("The number :", second)
list = [first,second]
while True:
    new = list[-1] + list[-2]
    if new >100:
        break
    list.append(new)
    print("The number :",new)