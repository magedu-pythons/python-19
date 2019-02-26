#!/usr/local/python3/bin/python3
a = (('a'), ('b'))
b = (('c'), ('d'))
c = zip(a, b)
def test():
    lst = list(map(lambda tub: {tub[0]:tub[1]}, c))
    print(lst)

#test()

