'给定一个整型列表，如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11 '
import datetime
from functools import wraps

def logger(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		start = datetime.datetime.now()
		ret = fn(*args, **kwargs)
		delta = (datetime.datetime.now() - start).total_seconds()
		print('{} tooks {}s'.format(fn.__name__,delta))
		return  ret
	return wrapper

@logger
def sum_townums(src:list, target:int):
	length = len(src)
	flag = [False] * length
	ret = []
	for i in range(length):
		if flag[i]:
			continue
		for j in range(i,length):
			if src[i] + src[j] == target:
				flag[i], flag[j] = True , True
				ret.append((src[i],src[j]))
				break
	return ret

print(sum_townums([1, 5, 2, 7, 4, 9],11))