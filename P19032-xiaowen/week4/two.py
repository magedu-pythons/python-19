#!/usr/local/python3/bin/python3
s = "esfhkffklrnvsdvc"
a = set(s) #去重
for i in a: 
    print("{}: {}".format(i,s.count(i)))
