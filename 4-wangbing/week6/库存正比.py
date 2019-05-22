'''2、已知仓库中有若干商品，以及相应库存，类似：
袜子，10
鞋子，20
拖鞋，30
项链，40
要求随机返回一种商品，要求商品被返回的概率与其库存成正比。请描述实现的思路或者直接写一个实现的函数'''

import random

items_dict = {'socks': 10, 'shoes': 30, 'slipper': 20, 'necklace': 40}
count = sum(items_dict.values())


def probility() -> str:
	items = []
	for k,v in items_dict.items():
		pre = [k] * int(100 * v / count)
		items.extend(pre)
	return random.choice(items)

print(probility())
