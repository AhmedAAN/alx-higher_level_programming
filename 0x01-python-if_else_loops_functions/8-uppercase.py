#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            print(f"{ord(ch)-32:c}", end="")
        else:
            print(f"{ord(ch):c}", end="")
