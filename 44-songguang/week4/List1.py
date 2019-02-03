Lst1=[]
while True :# 读取列表，
    Temp=input()
    if Temp=='':#不输数据，直接按回车完成列表输入
        break
    Lst1.append(Temp)
print(Lst1)#显示列表
Dt=input()#读取查找元素
Flag=0
for i in range(0,len(Lst1)):#判断元素是否在列表中
    if Lst1[i]==Dt:
        Flag=1
        break #找到就退出，节省运算
print(Flag)