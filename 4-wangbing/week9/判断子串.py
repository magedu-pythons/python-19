# def substr(s1:str, s2:str):
# 	len1 = len(s1)
# 	len2 = len(s2)
#
# 	if len1 > len2:
# 		return None
# 	else:
# 		sub = len2 - len1
# 		for i in range(0, sub + 1):
# 			if s1 == s2[i: i+len1]:
# 				return i
# 		else:
# 			return None
#
#
# print(substr(' ','3s 9'))


'方法2 动态规划法'

def substr(s1:str, s2:str):
	len1 = len(s1)
	len2 = len(s2)
	ret = [[0] * len2 for i in range(len1)]  # 这里list外面不可以用*len2

	index,step = 0, 0

	for i ,x in enumerate(s1):
		for j,y in enumerate(s2):
			if x == y:
				if i > 0 :
					ret[i][j] =  ret[i-1][j-1] +1
				else:
					ret[i][j] = 1
				if ret[i][j] > step:
					index = j		   #截取终止点
					step = ret[i][j]   #截取长度
	# print(*ret, sep='\n')
	# return s2[ index +1 - step :index+1]
	return  index - step + 1

print(substr('abcdef','abcd'))
print(substr(' ','3s 9'))