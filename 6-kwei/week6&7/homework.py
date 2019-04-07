#1.打乱一个排好序的list对象alist,alist=[1,2,3,4,5]
alist=[1,2,3,4,5]
def disrupt( alist:list ):
    import random
    new_list = []
    n = len(alist)
    for i in random.sample( range(0,n), n ):
        new_list.append( alist[i] )
    return new_list

#test
print(disrupt(alist))
print(alist) #不改变原alist

#---------------------------------------------------------------------
#2.已知仓库中有若干商品，以及相应库存，类似：
#袜子，10    鞋子，20    拖鞋，30    项链，40
#要求随机返回一种商品，要求商品被返回的概率与其库存成正比。请描述实现的思路或者直接写一个实现的函数 
raw_data = { '袜子':10,'鞋子':20,'拖鞋':30,'项链':40 }

def ran_ret( raw_data:dict ):
    import random
    total = 0 
    for i in raw_data.values():
        total += i
    data = {}
    flag = 1
    for key,value in raw_data.items():
        for i in range( int((value/total)*10) ):
            data[flag] = key
            flag += 1
    print(data)
    return data[random.randint(1,10)]

#test
print(ran_ret(raw_data))

#---------------------------------------------------------------------
#3.现有两元祖 (('a'),('b')),(('c'),('d')) ,请使用Python中的匿名函数生成列表 [ {'a':'c'｝,{'b':'d'}]
fun = lambda x,y : [ {x[0]:y[0]},{x[1]:y[1]} ]

#test
print(fun( (('a'),('b')),(('c'),('d')) ))

#---------------------------------------------------------------------
#4.输入一个英文句子,翻转句子中的单词顺序,但单词内字符的顺序不变 
sample = '''index modules | next | previous |  Python » 3.5.3 Documentation » The Python Standard Library » 11. File and Directory Access » 
11.2. os.path — Common pathname manipulations'''
def reverse_sentence( sample:str ):
    res = str()
    one = str()

    for s in reversed(sample):
        if s.isalpha():
            one = one+s
        if not s.isalpha():
            for c in reversed(one):
                res = res + c
            res = res + s
            one = str()
            
    for c in reversed(one):
        res = res + c
        
    return res

#test
print( reverse_sentence( sample ) )



"""
(0 + 0)

    
    good!
"""