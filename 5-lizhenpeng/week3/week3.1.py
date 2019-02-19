#coding=UTF-8
# 1.打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        if j==i:
            print(j,"*",i,"=",j*i,sep='')
        elif j*i < 10:
            print(j,"*",i,"=",j*i,'  ',sep='',end='')
        else:
            print(j,"*",i,"=",j*i,' ',sep='',end='')
#end
#2.打印菱形
n=7
j=n//2
for i in range(1,n+1,2):
    print(' '*j+'*'*i)
    j-=1
k=1
for i in range(n-2,0,-2):
    print(' '*k+'*'*i)
    k+=1
#end
