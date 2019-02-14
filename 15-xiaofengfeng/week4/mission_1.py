#1、给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0

list = [1,2,3,4,5,6,7,8,9,10,"x"]
###########################
if "x" in list:
    print(1)
else:
    print(0)
##########################
def listindex(list,x):
    if x in list:
        return 1
    else:
        return 0
a = listindex(list,"x")
print(a)

