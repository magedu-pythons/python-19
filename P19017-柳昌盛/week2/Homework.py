# 2、打印出100以内的斐波那契数列，使用2种方法实现
# 2-method1
Fib_list = [1, 1]
i = 0
while 1:
    if Fib_list[i]+Fib_list[i+1] < 100:
        Fib_list.append(Fib_list[i]+Fib_list[i+1])
        i += 1
    else:
        break
print(Fib_list)
# 2-method2


def fibonacci(n):
    if n < 0:
        return
    elif n == 1 or n == 0:
        fibonacci(n-1)
        return Fibonacci_list.append(1)
    else:
        fibonacci(n-1)
        return Fibonacci_list.append(Fibonacci_list[n-1]+Fibonacci_list[n-2])


Fibonacci_list = []
fibonacci(10)
print(Fibonacci_list)

# 3、使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上
import random
sett = set()
s = 'abcdefghigklmnopqrstuvwxyz1234567890'
while 1:
    s1 = ''
    for i in range(8):
        s1 += random.choice(s)
    sett.add(s1)
    if len(sett) == 100:
        break
print(sett)



"""
(0 + 0)

    good
"""