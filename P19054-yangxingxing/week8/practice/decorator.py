def logger(func):
    def wrapper(*args, **kwargs):
        print(*args, **kwargs)
        ret = func(*args, **kwargs)
        print('-------------')
        return ret
    return wrapper

@logger
def add(x, y):
    return x * y

print(add(2, 3))




