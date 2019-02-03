#!/usr/local/python3/bin/python3
n = input(">>> ")
f = n[::-1]
if f == n:
    print("{} is yes".format(n))
    try:
        c = int(n)
        print(c)
    except ValueError:
        print("you must enter number!!")
else:
    print('not')
