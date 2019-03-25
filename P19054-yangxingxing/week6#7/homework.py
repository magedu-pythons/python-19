import random

# 1、 打乱一个排好序的列表
alist = [1, 2, 3, 4, 5]
random.shuffle(alist)
print(alist)

# 2、
'''
已知仓库中有若干商品，以及相应库存，类似：
袜子，10
鞋子，20
拖鞋，30
项链，40
要求随机返回一种商品，要求商品被返回的概率与其库存成正比。请描述实现的思路或者直接写一个实现的函数 
'''
'''
思路: 某件商品/商品总数, 乘于1000是为了更精确，乘得越大越精确， 避免一些小数， 
math.ceil 避免0.3, 0.0001之类的数导致概率为0.
'''
import math
def get_one():
    comm = {'socks': 10, 'shoes': 20, 'slipper': 30, 'necklace': 40}
    total = sum(comm.values())
    comm_list = [k for k, v in comm.items() for _ in range(math.ceil(v * 1000 / total))]
    return random.choice(comm_list)

print(get_one())

# 3、 现有两元祖 (('a'),('b')),(('c'),('d')) ,请使用Python中的匿名函数生成列表 [ {'a':'c'｝,{'b':'d'}]
tuple1 = ('a', 'b')
tuple2 = ('c', 'd')
#list1 = [{x: y} for x, y in zip(tuple1, tuple2)]
list1 = [{x: y} for x, y in map(lambda x: (tuple1[x], tuple2[x]), range(len(tuple1)))]

print(list1)

# 4、输入一个英文句子,翻转句子中的单词顺序,但单词内字符的顺序不变
dd = "What's the most resilient parasite, one, two, three?"
new_str = ''
for i in reversed(dd.split()):
    if i.endswith(','):
        i = ',' + i[:-1]
    elif i.endswith('!'):
        i = '!' + i[:-1]
    elif i.endswith('?'):
        i = '?' + i[:-1]
    elif i.endswith('.'):
        i = '.' + i[:-1]
    new_str = new_str + ' ' + i
print(new_str)






