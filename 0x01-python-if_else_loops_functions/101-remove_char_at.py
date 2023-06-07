#!/usr/bin/python3
def remove_char_at(str, n):
    count = 0
    final = ""
    for i in str:
        if count != n:
            final += i
        count += 1
    return (final)
