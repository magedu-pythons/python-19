# 1、打印出100以内的斐波那契数列，使用2种方法实现

def fibonacci_1(num: int):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    a = 0
    b = 1
    for i in range(num):
        a, b = b, a+b
    print(a, b)


def fibonacci_2(num: int):
    if num <= 1:
        return num

    return fibonacci_2(num-1) + fibonacci_2(num-2)