# @Time    : 2019/1/19 19:19
# @Author  : HJW - biubiu ！！！
#第三周作业：
# 2、打印出100以内的斐波那契数列，使用2种方法实现
# 3、使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上

# 2、打印出100以内的斐波那契数列，使用2种方法实现
#---------------------方法1------------------------
#使用列表解释式来做，因为界限不确定，先取一个较大的范围range（1000），因为range是一个惰性可迭代对象，相对来说也不耗内存
fiblist=[1,1]
[fiblist.append(fiblist[i]+fiblist[i+1]) for i in range(1000) if (fiblist[-2]+fiblist[-1]) <100]
print(fiblist)
#---------------------方法2----------------------------
fiblist2=[1,1]
while True:
    if (fiblist2[-2]+fiblist2[-1])>100:
        break
    fiblist2.append(fiblist2[-2]+fiblist2[-1])
else:
    print('finished') #，老师，这里永远不会执行这一步，我想要练习一下else
print(fiblist2)

# 3、使用 Python 实现随机生成 200 无重复激活码（或者优惠券），字符串长度大于5以上
# '1'=chr(49) '9'=chr(57)   'a'=chr(97)  'z'=chr(122)  'A'=chr(65)  'Z'=chr(90)
import string
import random
allstr=string.digits
allstr +=string.ascii_lowercase
allstr +=string.ascii_uppercase
# print(allstr)
# code=[]
activecode=[''.join([random.choice(allstr) for _ in range(random.randint(5,9))]) for _ in range(200) ]
print(activecode)



"""
(0 + 0)
    这里的else 是在没有被break的时候执行
    优惠码会存在重复，请参考答案

"""

