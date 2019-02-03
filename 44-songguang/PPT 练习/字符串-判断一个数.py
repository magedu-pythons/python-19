x=input('>>>')
D=x.lstrip('0')#扒掉前面的0
L=len(D)
print('这是一个{}位数'.format(L))
for i in range(L):
    flag=1
    Count=0
    for k in range(i):
        if D[k]==D[i]:
            flag=0
            break# 在前面找到重复数字，退出不再找
    if flag==0:
        continue# 跳转到下一位数
    for j in range(i,L):
        if D[j]==D[i]:
            Count += 1 # 后面出现的次数统计
    print('{}出现了{}次'.format(D[i],Count))
print('各个位上的数分别是：')
for i in range(L):
    print( D[L-i-1] )
