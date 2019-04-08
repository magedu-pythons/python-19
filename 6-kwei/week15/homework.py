# # 1、python 中如何实现单例模式，尽可能多的写出实现方式
# # 1) 使用模块, 加载模块时只加载一次, 不会重复加载
# # singleton.py
#
#
# class Singleton(object):
#     def foo(self):
#         pass
#
#
# singleton = Singleton()
#
#
# # from singleton import singleton
#
#
# # 2) 使用装饰器, 保证实例不重复
# def singleton(cls):
#     _instance = {}
#
#     def _singleton(*args, **kwargs):
#         if cls not in _instance:
#             _instance[cls] = cls(*args, **kwargs)  # instance
#         return _instance[cls]  # 如果存在就直接调取
#
#     return _singleton
#
#
# @singleton  # A(1) = singleton(A)(1)
# class A(object):
#     def __init__(self, x=0):
#         self.x = x
#
#
# a1 = A(1)
# a2 = A(3)
#
# # 3) 使用类
# import time
# import threading
#
#
# class Singleton:
#     _instance_lock = threading.Lock()
#
#     def __init__(self):
#         time.sleep(1)
#
#     @classmethod
#     def instance(cls, *args, **kwargs):
#         if not hasattr(Singleton, "_instance"):
#             with Singleton._instance_lock:
#                 if not hasattr(Singleton, "_instance"):
#                     Singleton._instance = Singleton(*args, **kwargs)
#         return Singleton._instance
#
#
# def task(arg):
#     obj = Singleton.instance()
#     print(obj)
#
#
# for i in range(10):
#     t = threading.Thread(target=task, args=[i, ])
#     t.start()
# time.sleep(20)
# obj = Singleton.instance()
# print(obj)
#
# # 4) 基于__new__方法实现
# import threading
#
#
# class Singleton(object):
#     _instance_lock = threading.Lock()
#
#     def __init__(self):
#         pass
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(Singleton, "_instance"):
#             with Singleton._instance_lock:
#                 if not hasattr(Singleton, "_instance"):
#                     Singleton._instance = object.__new__(cls)
#         return Singleton._instance
#
#
# obj1 = Singleton()
# obj2 = Singleton()
# print(obj1, obj2)
#
#
# def task(arg):
#     obj = Singleton()
#     print(obj)
#
#
# for i in range(10):
#     threading.Thread(target=task, args=[i, ]).start()
#
# # 5) 元类的使用
# import threading
#
#
# class SingletonType:
#     _instance_lock = threading.Lock()
#
#     def __call__(cls, *args, **kwargs):
#         if not hasattr(cls, "_instance"):
#             with SingletonType._instance_lock:
#                 if not hasattr(cls, "_instance"):
#                     cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
#         return cls._instance
#
#
# class Foo(metaclass=SingletonType):
#     def __init__(self, name):
#         self.name = name
#
#
# obj1 = Foo('name')
# obj2 = Foo('name')
#
# print(obj1, obj2)
#
# # 2、两个有序数组，分别拥有m和n的长度，求其合并后的第k个值
# # 默认升序
# a = [1, 2, 2, 4, 7, 9, 10]
# b = [3, 5, 8, 20]
# k = 5
#
#
# def find_k(a, b, k):
#     indexa = 0
#     indexb = 0
#     if k > len(a) + len(b):
#         return -1
#     for _ in range(k):
#         if a[indexa] >= b[indexb]:
#             rec = b[indexb]
#             indexb += 1
#         else:
#             rec = a[indexa]
#             indexa += 1
#     return rec
#
#
# print(find_k(a, b, k))


# 3、 将逆转波兰式转化为中序表达式（自行查询逆波兰式、中序表达式相关资料）
# 举例: 输入 {"5", "8", "4", "/", "+"}，输出 "(5+(8/4))"

# 今天刚刚实现了栈, 拿出我实现的栈来解决这个问题
class SequentialStack:
    def __init__(self, length):
        self.length = length
        self.init = length
        self.space = [0] * length
        self.number = 0

    def push(self, data, dyna=False):
        if not dyna:  # 默认不扩容
            if self.number >= self.length:
                return -1
        else:  # 如果扩容
            if self.number >= self.length:
                self.space += [0] * self.length
                self.length += self.length
        self.space[self.number] = data
        self.number += 1

    def pop(self):
        if self.number == 0:
            return -1
        self.number -= 1
        return self.space[self.number]

    def read_last(self):
        if self.number == 0:
            return 'no content'
        return str(self.space[self.number - 1])

    def clean(self):
        self.length = self.init
        self.number = 0

    def __repr__(self):
        return 'stack space: {},number: {},length: {}'.format(','.join(map(lambda x: str(x), self.space)),
                                                              self.number,
                                                              self.length
                                                              )

    __str__ = __repr__


def change(everse_polish):
    stack_of_number = SequentialStack(10)
    for n in everse_polish:
        if n.isdigit():
            stack_of_number.push(n, True)
        else:
            num2 = stack_of_number.pop()
            num1 = stack_of_number.pop()
            stack_of_number.push('({}{}{})'.format(num1, n, num2), True)
        print(stack_of_number, n)
    return stack_of_number.pop()

#test
print(change(["5", "8", "4", "/", "+"]))
# 出入一定要有序, 否则会出错
