num1 = 0
num2 = 1

while True:
    print(num2)
    num1,num2 = num2,num1+num2
    if num2 >= 100:
        break