#1、问题描述：一个5位数，判断它是不是回文数。
while True :
    number = input("请输入一个5位数：")
    number1 = number[:]
    number2 = number[::-1]  #字符串取反
    if number1 == number2 :
        print("您输入的{}是回文数".format(number))
    else:
        print("您输入的{}不是回文数".format(number))





"""
(0 + 0)

    作业写到一个文件里面
"""

