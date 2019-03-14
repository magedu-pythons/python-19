#第一题解法1 打乱列表
Lst=[]
alst=[]
while True :
    Temp = input(">>>")
    if Temp == "" :
        break
    Lst.append(Temp)
print(Lst)
for i in range(len(Lst)):
    alst.append(Lst.pop())
print(alst)


#第一题解法2  打乱列表，会剔除重复元素
Lst=[]
aset=set()
while True :
    Temp = input(">>>")
    if Temp == "" :
        break
    Lst.append(Temp)
print(Lst)
for i in range(len(Lst)):
    aset.add(Lst[])
print(aset)

# 第二题  返回一种商品，概率和库存一样

import random
Adict = {"袜子": 10, "鞋子": 20, "拖鞋": 30, "项链": 40}
def Goods():  # 生成1-库存总量total的随机数， 在对应的区间范围返回字典的key，即商品名
    total = 0
    for v in Adict.values():
        total += v

    i = random.randint(1, total+1)
    print(i)
    sum = 0
    key = list(Adict.keys())
    print(key)
    for k in key: #通过遍历字典看，随机数是否在对应的商品区间，区间的大小等同于库存数，返回的几率与库存数量成正比
        sum += Adict[k]
        if i <= sum:
            break
    print(k)
    return k
Goods()


# 第三题   匿名函数
print((lambda x,y :[{x[0]:y[0]},{x[1]:y[1]}])((('a'),('b')),(('c'),('d'))))


#  第四题  反转一句英文

def  revwords():
    words = input (">>>")
    lst1=[]
    newword = ""
    lst1 = words.split()
    lst1.reverse()
    for i in lst1:
        newword += (i+" ")
    print(newword)

revwords()



