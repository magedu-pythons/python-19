#!/usr/local/python3/bin/python3
n = int(input("enter number: "))
if n < 0:
    print("you must enter a number greater than zero")
    exit(1)

a = 1
b = 1
print(a)
print(b)
for i in range(2,n):
    num = a+b
    b=a
    a=num
    print(num)




"""
(0 + 0)

    作业写到一个地方，参考week-demo
"""