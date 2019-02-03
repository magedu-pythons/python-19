import random
Lst1=[]
for i in range(20):
   Lst1.append(random.randrange(1,100))
print(Lst1)
for i in range(3):
    for j in range(20-i-1):
        if Lst1[j] > Lst1[j+1]:
            Lst1[j],Lst1[j+1]=Lst1[j+1],Lst1[j]
print(Lst1[19],Lst1[18],Lst1[17])