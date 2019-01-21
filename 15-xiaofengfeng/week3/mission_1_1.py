#打印出100以内的斐波那契数列，使用2种方法实现
first = 1
second = 1
print("The number :", first)
print("The number :", second)
while True:
    new = first + second
    if new >100:
        break
    first = second
    second = new
    print("The number :",new)





