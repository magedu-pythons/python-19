#!/usr/local/python/bin/python3
def findstr():
    str1=str(input("str1 >>>: "))
    str2=str(input("str2 ///: "))
    length1 = len(str1)
    length2 = len(str2)
    if str2 in str1:
        for i in range(length1):
            if str1[i:i+length2] == str2:
                return i
    else:
        return None
print(findstr())
