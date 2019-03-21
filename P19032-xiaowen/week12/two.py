#!/usr/local/pyton3/bin/python3
import os
import fnmatch

def findfile(dirname):
    filelist = []
    for parent, dirname, filename in os.walk(dirname):
        for i in filename:
            filelist.append(i)
    return fnmatch.filter(filelist, '*.py')
