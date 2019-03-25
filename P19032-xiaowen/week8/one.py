#!/usr/local/python3/bin/python3
def change():
    a = "1,2,3"
    b = str(a.split(",")).replace("'", '"')
    return b


print(change())
