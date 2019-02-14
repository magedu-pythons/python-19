#2、打印出100以内的斐波那契数列，使用2种方法实现
#1:
a = 1
b = 1
print(a)
print(b)
while True:
    c = a + b
    a = b
    b = c
    if c < 100:
        print(c)
    else:
        break

#2:
a = 1
b = 1
c = 1
print(a)
print(b)
while c <= 100:
    c += 1
    if c == a + b:
        print(c)
    else:
        continue
    a = b
    b = c




"""
(0 + 0)

    参考答案实现
"""