#方法1
L=[1,1]
while True:
    l=L[len(L)-1]+L[len(L)-2]
    if l >100:
        break
    L.append(l)
print(L)

#方法2
a=0
b=1
L=[]
while True:
    L.append(b)
    c=a+b
    a=b
    b=c
    if c >100:
        break
print(L)
