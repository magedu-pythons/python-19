import re
f = open('C:/Users/260139/Desktop/week4/story.txt','r')
data = f.read()
count = 0
print(data)
print(type(data))
data_list = re.findall(r'[a-zA-Z]+',data)
print(data_list)
print(len(data_list))