#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqueNumbers = set(my_list)
    total = 0
    for number in uniqueNumbers:
        total += number
    return total
