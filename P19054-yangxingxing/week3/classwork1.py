#/usr/bin/env python
#
# 1、 九九乘法表
for y in range(1, 10): 
    for x in range(1, y+1): 
        print('%s*%s=%s' % (x,y,y*x),end='\t') 
    print() 


# 2、 打印菱形
# 2.1、实际的以*号推起来，最大只能是奇数个*
def abc(num): 
    middle_num = num // 2 
    for i in range(num): 
        if i > middle_num: 
            tag_n = num - ((i - middle_num) * 2) 
        else: 
            tag_n = 1 + i * 2 
        spa_n = (num - tag_n) // 2 
        print(' ' * spa_n + '*' * tag_n + ' ' * spa_n)


# 2.2、在*号之间加一个空格，最大的数可以是任何数， 只是行数要加上所填充的空格数。
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

# 2.3、以对称方式打印菱形,i等于一侧的空格数
n = 9
e = -n//2 + 1
for i in range(e,n+e):
    if i <= 0:
        tag_num = n + i * 2
    else:
        tag_num = n - i * 2
    spa_num = (n - tag_num) // 2
    print(spa_num * ' ' + tag_num * '*' + spa_num * ' ')

#
# 2.3.1,  优化
n = 9
e = -(n//2)
for i in range(e,n+e):
    if i <= 0: i = -i
    tag_num = n - i * 2
    spa_num = i
    print(spa_num * ' ' + tag_num * '*')


# 2.4、abs绝对值菱形
n = 9
e = -(n//2)
for i in range(e,n+e):
    tag_num = n - abs(i) * 2
    spa_num = abs(i)
    print(spa_num * ' ' + tag_num * '*' + spa_num * ' ')


# 3、上下宽，中间窄的菱形. 对角三角形
# 3.1
n = 9
e = -(n//2)
for i in range(e,n+e):
    tag_num = abs(i) * 2 + 1
    spa_num = (n - tag_num) // 2
    print(spa_num * ' ' + tag_num * '*' + spa_num * ' ')

# 3.2 
n = 9
e = -(n//2)
for i in range(e,n+e):
    if i <= 0:
        spa_num = n + (i * 2 - 1)
    else:
        spa_num = n - (i * 2 + 1)
    tag_num = n - spa_num
    spa_num = spa_num // 2
    print(spa_num * ' ' + tag_num * '*' + spa_num * ' ')

# 3.3,  这里e不用负数的原因是： e-line_num 会出现负数， 而负数 乘 ' ' 为 ''。
n = 9
e = n // 2
for i in range(-e, n-e):
    line_num = -i if i < 0 else i
    print(' ' * (e-line_num) + '*' * (line_num * 2 + 1))




