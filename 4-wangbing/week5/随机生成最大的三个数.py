import random
def randominttop(n:int):
	return sorted([random.randint(1,10000) for i in range(20)], reverse=True)[:3]

print(randominttop(3))