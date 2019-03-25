#import string, random

# 生成新的列表，元素是现有列表的相邻两个元素的和.
#lst = [1,4,9,16,2,5,10,15]
#[lst[i]+lst[i+1] for i in range(len(lst)-1)]

# 99 乘法表
[print('{} * {} = {} {}'.format(y, x, x*y, '\n' if x == y else ' '), end='') for x in range(1, 10) for y in range(1, x+1)]

# 随机ID， id编号从0001开始.
#str_case = string.printable[10:36]
#str = ['{1:04}.{0}'.format(''.join([random.choice(str_case) for y in range(10)]), i) for i in range(1,101)]
#print(str)

