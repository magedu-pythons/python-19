#!/usr/local/python3/bin/python3
def max():
    lst=[1,2,5,7,4,9]
    tag = int(input("enter a number >>>: "))
    leng = len(lst)
    for i in range(leng-1):
        for j in range(i+1, leng):
            if lst[i] + lst[j] == tag:
                print(lst[i], lst[j])
