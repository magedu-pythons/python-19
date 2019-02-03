a = [1,2,[3,4,['abc','de',0,['ccc',1]]],999,100]
for i in range(len(a)):
    b=str(a[i])
    if b.count('ccc'):
        print(1)
        break
else:
    print(0)
