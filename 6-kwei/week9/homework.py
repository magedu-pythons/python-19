#1、实现一个函数用于判断字符串str2是否是str1的子串。如果是，则该函数返回str2在str1中首次出 现的地址；否则，返回None。

def is_substr(str1:str,str2:str): #判断str2是否是str1的子串
    flag = True
    lenstr1 = len(str1)
    lenstr2 = len(str2)
    if lenstr2 > lenstr1:
        print('The length of str2 cannot be greater than str1!')
    for i in range(0,lenstr1-lenstr2+1):
        for k,j in enumerate(range(i,i+lenstr2)):#str2[k]? str1[j]
            if str2[k] != str1[j]:
                flag = False
                break
        else:
            return i
    return None

#test
str1 = 'asdklfnasbbchd'
str2 = 'lfn'
addr = is_substr(str1,str2)
print(addr,str1[addr:addr+len(str2)],str2)

str1 = 'assdklfnasbbchd'
str2 = 's'
addr = is_substr(str1,str2)
print(addr,str1[addr:addr+len(str2)],str2)

str1 = 'assdklfnasbbchd'
str2 = 'awkkk'
addr = is_substr(str1,str2)
print(addr)

#--------------------------------------------------------------------------------------------------

#2、给定一个整型列表，请实现从其中找出2个数的和为某一个指定的值？
#如：lst =[1,5,2,7,4,9]，指定的目标值为11，可以从中找出 2和9之和为11

def find_tar(lst:list,target:int):
    length = len(lst)
    for i,num in enumerate(lst):
        for j in lst[i+1:length]:
            if num + j == target:
                print('{}和{}只和为{}'.format(num,j,target))
#一次循环作用值, 与每一次的作用值与该值后面的值进行检查

#test
lst =[1,5,2,7,4,9]
find_tar(lst,11)