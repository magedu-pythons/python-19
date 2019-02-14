#!/usr/bin/env python
## 给出任意一个列表，请查找出x元素是否在列表里面，如果存在返回1，不存在返回0
lst = []
while True:
    param = input(">>>('quit' for exit)")
    if param == "quit":
        break
    else:
        lst.append(param)

target = input("x>>>")  
for i in lst:
    if i == target:
        print(1)
        break
else:
    print(0)      
    
