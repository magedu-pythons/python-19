#!/usr/local/python3/bin/python3
n = int(input("enter number: "))
if n < 0:
    print("you must enter a number greater than zero")
    exit(1)

a = 1
b = 1
print(a)
print(b)
while True:
    c = a + b
    if c > n: break
    b = a
    a = c
    print(c)
