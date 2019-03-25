# 求阶乘
def factorial2(n):
    if n <= 1:
        return 1
    else:
        return n * factorial2(n-1)
print(factorial2(10))

# 数字逆序放入列表中
def reverse_order(num):
    remainder = num % 10
    if remainder == num:
        return [num]
    else:
        return [remainder] + reverse_order(num // 10)

print(reverse_order(10128023))

# 猴子吃桃
def monkey_peach(num, total):
    if num > 1:
        total = (total+1) * 2
        return monkey_peach(num-1, total)
    else:
        return (total+1) * 2
print(monkey_peach(9, 1))


