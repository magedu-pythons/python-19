
import random
list = []
for number in range(10): #数字
    list.append(str(number))
for lowercase in range(97,123): #小写
    list.append(chr(lowercase))
for majuscule in range(65,91): #大写
    list.append(chr(majuscule))
for act_code in range(200):
    b = ""
    for s in range(6):
        a = random.choice(list)
        b += a
    print(b)