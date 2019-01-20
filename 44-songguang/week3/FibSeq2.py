a=1
b=1
c=0
fb=[1,1]
while a+b<100 :
    c=a+b
    fb.append(c)
    a=b
    b=c
print(fb)