sub1 = 'defghpp'
sub2 = 'deffghppab'


max_dict = {}
for i in range(len(sub1)):
    count = 0
    for n in range(len(sub2)):
        if sub1[i] == sub2[n]:
            count += 1
        else:
            max_dict[count] = i

print(max_dict)

