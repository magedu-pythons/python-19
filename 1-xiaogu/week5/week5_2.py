import random
lst = []
for i in range(20):
	x = random.randint(0,100)
	lst.append(x)
print(lst)
for i in range(20):
	for j in range(19):
		if lst[j] > lst[j+1]:
			lst[j+1], lst[j] = lst[j], lst[j+1]
		else:
			continue
lst.reverse()
print(lst[0], lst[1], lst[2])

