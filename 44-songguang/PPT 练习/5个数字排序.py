a=[0,0,0,0,0]
for i in range(5):
    a[i]=int(input('>>>'))
for i in range(5):
    print('{}是一个{}位数'.format(a[i],len(str(a[i]))))
for i in range(5):
    for j in range(5-i-1):
        if a[j+1]<a[j]:
            a[j],a[j+1]=a[j+1],a[j]
for i in range(5):
    print(a[i])

