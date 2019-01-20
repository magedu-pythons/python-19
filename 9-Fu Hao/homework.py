#使用两种方法实现100以内的斐波那契数列
#first


a,b = 0,1
print(a,b,sep = '\n')
while True:
	c = a + b 
	b,a = c,b 
	if c > 100:
		break
	print(c)
	
 
#second


a,b = 0,1
print(a,b,sep = '\n')
for i in range(100):
	c = a + b 
	b,a = c,b 
	if c > 100:break
	print(c)

	
	
	
#使用Python随机生成200个无重复字符串长度大于5的激活码
import random
for i in range (200):
	str = ''
	for j in range (5):
		str += random.choice('abcdefghijklmnopqrstuvwxyz')
	print(str)
#没有解决无重复的问题