#!/usr/local/python3/bin/python3
import random
wazi = ['wz'] * 100
xiezi = ['xz'] * 200
tuoxie = ['tx'] * 300
xianglian = ['xl'] * 400
def test():
    al = wazi + xiezi + tuoxie + xianglian
    choose = random.sample(al, 100)
    print(choose.count('wz'))
    print(choose.count('xz'))
    print(choose.count('tx'))
    print(choose.count('xl'))
test()
