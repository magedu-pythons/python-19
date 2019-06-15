# 2、上下文管理是什么？请实现一个python 类，具有上下文管理功能

class A:
    def __init__(self, name):
        self.name = name
        print('__init__')

    def __enter__(self):
        print('__enter__', self.name)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')


with A('ba') as a:
    print('hello', a)

with A('a'):
    print('hi')
