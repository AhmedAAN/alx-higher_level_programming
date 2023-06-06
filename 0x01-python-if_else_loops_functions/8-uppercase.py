#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            x = ord(ch)-32
        else:
            x = ord(ch)
        print("{0:c}".format(x), end="")
    print("")
