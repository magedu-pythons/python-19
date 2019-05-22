import random

def disruptsort(lst):
	random.shuffle(lst)
	return lst

print(disruptsort([1,3,5,7,8,9,0]))
