# coding=UTF-8
# 2. 打印100以内的斐波那契数列
m=0
n=1
print(0)
print(1)
while True:
	x=n+m
	if x > 100: break
	m=n
	n=x
	print(x)
