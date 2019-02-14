# 2、使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上
import string
import random

def gen_promotion_code(num: int, length: int):
    """

    :param num:     生成的优惠券数量
    :param length:  生成的优惠券长度
    :return:
    """
    # string模块引入字符串和数字作为生成基数
    sd = string.ascii_letters + string.digits
    s = set()
    while len(s) < num:
        promotion_code = ''.join(random.sample(sd, length))
        s.add(promotion_code)
    return s

print(gen_promotion_code(200, 9))
print('abc %s %d' % ('as', 11))
print('wqwqwq{},{}'.format('aa', 11))