# 现有两元祖 (('a'),('b')),(('c'),('d')) ,请使用Python中的匿名函数生成列表 [ {'a':'c'｝,{'b':'d'}]

t1, t2 = ('a', 'b'), ('c', 'd')

func = lambda tup1, tup2: [{tup1[0]: tup2[0]}, {tup1[1]: tup2[1]}]
print(func(t1, t2))