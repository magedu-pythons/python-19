# 2、实现pow函数，分析其时间复杂度

def my_pow(a, n):
    if a == 0 or a == 1 or n == 1:
        return a

    if a == -1:
        if n % 2 == 0:
            return 1
        else:
            return -1

    if n == 0:
        return 1

    if n < 0:
        return 1 / my_pow(a, -n)

    val = my_pow(a, n // 2)

    if n % 2 == 0:
        return val * val
    return val * val * a


# test
print(my_pow(3, 3))
