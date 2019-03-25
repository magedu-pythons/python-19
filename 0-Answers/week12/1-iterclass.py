class IterC:
    def __init__(self):
        self.lst = []

    def __iter__(self):
        yield from self.lst


# test
iter_c = IterC()
iter_c.lst.extend([2, 3, 4, 5])
for c in iter_c:
    print(c)
