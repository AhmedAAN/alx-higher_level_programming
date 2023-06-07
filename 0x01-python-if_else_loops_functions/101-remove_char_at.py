#!/usr/bin/python3
def remove_char_at(str, n):
    count = 0
    for i in str:
        if count != n:
            print(f"{i}", end="")
        count+=1
    print("")
