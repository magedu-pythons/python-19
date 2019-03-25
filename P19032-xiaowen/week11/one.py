#!/usr/local/python3/bin/python3

def new_counter(x):
    y = x
    def new_counters():
        nonlocal y
        y += 1
        return y
    return new_counters
c1 = new_counter(10)
c2 = new_counter(20)
print(c1(),c2(),c1().c2())

