number = int(input('please enter the number for calculating !:'))
i = 0
j = 1
index = 1
num = i + j
print(f"the {1}th integer : {1}")
while num < number:
    print(f'the {index + 1}th integer : {num}')
    index += 1
    i = j
    j = num
    num = i + j
print('there is total {} integer satisfy the result'.format(index))

# test
# please enter the number for calculating !:100

