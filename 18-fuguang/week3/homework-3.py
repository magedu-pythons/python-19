import random
random_lst = []
count = 0
while True:
    str = ''
    count += 1
    for i in range(5):
        str1 = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        str2 = random.choice(str1)
        str += str2
    if count > 100000:
        break
    if str in random_lst:
        continue
    else:
        random_lst.append(str)
    if len(random_lst) >= 200:
        break
for i in random_lst:
    print(i)





"""
(0 + 0)


"""

