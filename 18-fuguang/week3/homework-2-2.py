lst = [1,1]
while True:
    num = lst[-1] + lst[-2]
    if num >=100:
        break
    lst.append(num)
print(lst)