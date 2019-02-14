def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
for i in range(1,101):
    if Fibonacci(i)>100:
        break
    print(Fibonacci(i))
	
	

a = 1
b = 1
print(a)
print(b)
for count in range(99):
    a,b=b,a+b
    if b>100:
        break
    print(b)
	
	
	
	
import random

sequence = ''
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-_*.,?;'':""[]{}\|!@#$%^&*()"
for m in range(200):
	num = random.randint(5,30)
	for i in range(num):
		a = random.choice(chars)
		sequence += a
	print(sequence)
	sequence = ''

	


	

