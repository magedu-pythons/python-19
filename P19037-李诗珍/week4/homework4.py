#给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0


num = int(input('Please input num : '))                                     #input num

newlist = [input('Please input a element : ') for i in range(num)]          #input element

find = input('Please input find a element : ')                              #input find element

if find in newlist:                                                         #find element
    print('{} in list!'.format(find))
else:
    print('{} not in list!'.format(find))



#任一个英文的纯文本文件，统计其中的单词出现的个数。

newstr = input('Please input a English plain text file : ')                 #input txt
d = {}                                                                      #defind dict
for i in newstr:                                                            #append k-v
    if i not in d.keys():
        d[i] =1
    else:
        d[i] += 1

print(d)                                                                    #print dict 打印字典方法一

#for i in d:                                                                #print dict  打印字典方法二
#    print('{} frequency of occurrence is {}'.format(i,d[i]))