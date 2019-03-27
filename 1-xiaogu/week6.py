#一：
import random
alist = [1, 2, 3, 4, 5]

random.shuffle(alist)
print(alist)
	
#二：
import random
lst_keys = []
lst_values = []
lst_scale = []

def stuff_callback(**kwarg):
	# print(kwarg)
	sum = 0
	scale = 0
	random_choice = random.random()
	print(random_choice)
	for i in kwarg.values():
		lst_values.append(i)
		sum += i 
	for i in kwarg.keys():
		lst_keys.append(i)
	print(lst_keys)
	for i in range(len(lst_values)):
		scale += lst_values[i]
		lst_scale.append(scale / sum )
	for i in range(len(lst_scale)):
		if random_choice< lst_scale[i]:
			break
	print(lst_keys[i])
	return lst_keys[i]
	
	
	
	

stuff_callback(袜子=10,鞋子=20,拖鞋=30,项链= 40)