#使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上
#6位激活码
import random
for i in range(200):
    e = ""
    for j in range(6):
        a = str(random.randint(0,9))
        b = chr(random.randint(97,122)) #   a - z
        c = chr(random.randint(65,90))  #   A - Z
        d = random.choice([a,b,c])
        e += d
    print(e)
