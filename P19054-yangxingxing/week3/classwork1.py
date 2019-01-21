#/usr/bin/env python
#
# 1、 九九乘法表
for y in range(1, 10): 
    for x in range(1, y+1): 
        print('%s*%s=%s' % (x,y,y*x),end='\t') 
    print() 


# 2、 打印菱形
# 1、实际的以*号推起来，最大只能是奇数个*
def abc(num): 
    middle_num = num // 2 
    for i in range(num): 
        if i > middle_num: 
            tag_n = num - ((i - middle_num) * 2) 
        else: 
            tag_n = 1 + i * 2 
        spa_n = (num - tag_n) // 2 
        print(' ' * spa_n + '*' * tag_n + ' ' * spa_n)


# 2、在*号之间加一个空格，最大的数可以是任何数， 只是行数要加上所填充的空格数。
def abc_c(num,space=1): 
    num = num + ((num - 1)*space) 
    middle_num = num // 2 
    for i in range(num): 
        if i > middle_num: 
            tag_n = num - ((i - middle_num) * 2) 
        else: 
            tag_n = i * 2 + 1 
        spa_n = (num - tag_n) // 2 
        print(' ' * spa_n,end='') 
        for n in range(1,tag_n+1): 
            if n & 1: 
                print('*',end='') 
            else: 
                print(' ',end='') 
        print(' ' * spa_n)

abc(7)
abc_c(6)
abc_c(6,3)



