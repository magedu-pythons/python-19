#2、随机生成20个数字，并且筛选出其中最大的3个数
import random
min = int(input("输入一个区间下限："))
max = int(input("输入一个区间上限："))
numbers_count = int(input("选取个数："))

number_list = [i for i in range(min,max+1)]
choice_number = random.sample(number_list,numbers_count)
print(choice_number)
choice_number.sort(reverse=True)
print("最大数:{}，第二位:{},第三位:{}".format(choice_number[0],choice_number[1],choice_number[2]))
