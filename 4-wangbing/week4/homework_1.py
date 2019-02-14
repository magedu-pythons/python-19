lst=[1,2,3,'q','y','xx',['x','y']]
flag=False#添加标记
for i in range(len(lst)):
    if 'x' == lst[i]:
        flag=True
    if isinstance(lst[i],list):#列表嵌套列表时
        if 'x' in lst[i]:
            flag=True
if flag:
    print(1)
else:
    print(0)