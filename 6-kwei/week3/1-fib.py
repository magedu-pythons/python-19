#循环
def fib(N):
    f1 = 0
    f2 = 1
    while f2 < N:
        print(f2,end = ' ')
        f1,f2 = f2,f2+f1
fib(100)
print()

#递归
def fib(n):
    if n < 2 :
        return n
    return fib(n-1)+fib(n-2)
def print_fib(N):
    i = 1
    while True:
        f = fib(i)
        if f < N:
            print(f,end = ' ')
            i += 1
        else:
            break
print_fib(100)
print()

#cache
import functools
@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n-1)+fib(n-2)
def print_fib(N):
    i = 1
    while True:
        f = fib(i)
        if f < N:
            print(f,end = ' ')
            i += 1
        else:
            break
print_fib(100)




"""
(0 + 0)

    good!
"""



