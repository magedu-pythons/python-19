f2=[]
while True :
        f1=input()# 粘贴文本内容
        if f1=='':
            break # 输入空字符窜完成输入
        f3=f1.replace(',',' ').replace('.',' ').split()# 把每一段转化为一个列表
        f2=f2+f3 #每个列表合并到一起
        f3=[]
print(len(f2))




"""
(0 + 0)

        作业按照week-demo方式命名
"""

