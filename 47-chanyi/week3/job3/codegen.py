#!/usr/bin/env python
#
## 使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上

import random,string
src =  string.ascii_letters + string.digits

for i in range(200):
    str_code=''.join(random.sample(src,6))
    print(str_code)
