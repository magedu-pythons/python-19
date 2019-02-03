import re

f = open("Story.txt","r")
lst = []
for line in f:
    st = re.split('[ ,.";\']',line)
    for ch in st:
        if ch == '' or ch == '\n':
            continue
        else:
            lst.append(ch)

lst.sort()
dic = {}
for i in lst:
    dic[i] = lst.count(i)

for k,v in dic.items():
    print(k,v)