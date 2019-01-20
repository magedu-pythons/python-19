# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
# 方法一
first_num = 0
second_num = 1
length = 100

for i in range(100):
    print(first_num)
    next_num = first_num + second_num
    if next_num > length:
        print(second_num)
        break
    else:
        first_num = second_num
        second_num = next_num

print('***'*10)

# 方法二
limit = 100

def fib(num):
    result = [0,1]
    for n in range(num-2):
        result.append(result[-2] + result[-1])
        if result[-1] > limit:
            result.pop()
            break
    return result

for a in fib(100):
    print(a)