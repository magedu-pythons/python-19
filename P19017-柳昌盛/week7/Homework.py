# 1、打乱一个排好序的list对象alist，alist=[1,2,3,4,5]
import random
alist = [1, 2, 3, 4, 5]
random.shuffle(alist)
print(alist)
# 2、已知仓库中有若干商品，以及相应库存，类似：
# 袜子，10         1
# 鞋子，20         2-3
# 拖鞋，30         4-6
# 项链，40         7-10
# 要求随机返回一种商品，要求商品被返回的概率与其库存成正比。请描述实现的思路或者直接写一个实现的函数


def ret():
    num = random.randint(1, 10)
    if num >= 7:
        return '项链'
    elif 4 <= num <= 6:
        return '拖鞋'
    elif 2 <= num <= 3:
        return '鞋子'
    else:
        return '袜子'


# 3、# 现有两元祖 (('a'),('b')),(('c'),('d')) ,请使用Python中的匿名函数生成列表 [ {'a':'c'｝,{'b':'d'}]
# q = [lambda {x1=y1}]


# 4、输入一个英文句子,翻转句子中的单词顺序,但单词内字符的顺序不变
def rev(strs):
    a = strs.split(' ', -1)
    a.reverse()
    strs = ' '.join(a)
    return strs


str1 = str(input('>>>'))
print(rev(str1))




"""
(0 + 0)

    第二题有错误，要按概率返回
"""