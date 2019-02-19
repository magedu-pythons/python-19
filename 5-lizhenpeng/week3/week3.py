# 2. 打印100以内的斐波那契数列
for i in range(1,101):
    if i==1 or i==2:
        m=1
        n=m
        print(n)
    elif i==3:
        x=n+m
        n=x
        print(x)
    else:
        x=n+m
        m=n
        n=x
        print(x)
