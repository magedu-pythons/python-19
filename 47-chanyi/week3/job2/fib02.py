#!/usr/bin/env python
#
fir=1
sec=1
print(fir,sec)
while True:
    val = fir+sec
    if val < 100:
        fir = sec
        sec = val
        print(val)
    else:
        break
