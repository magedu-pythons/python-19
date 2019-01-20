#!/usr/bin/env python
#
import random,string
src =  string.ascii_letters + string.digits

for i in range(200):
    str_code=''.join(random.sample(src,6))
    print(str_code)
