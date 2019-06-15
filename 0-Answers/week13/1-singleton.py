# 1、python 中如何实现单例模式，尽可能多的写出实现方式

# 在Python中模块变量本身是单例形式


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


# test
sing1 = Singleton()
sing2 = Singleton()

print(id(sing1), id(sing2))


# use decator
def singleton(cls):
    _instance = {}

    def wrap():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]

    return wrap


# test

@singleton
class A:
    pass


a1 = A()
a2 = A()
print(id(a1), id(a2))