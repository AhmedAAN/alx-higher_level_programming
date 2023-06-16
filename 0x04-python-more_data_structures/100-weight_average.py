#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    upper = 0
    lower = 0
    for tup in my_list:
        upper += tup[0] * tup[1]
        lower += tup[1]
    return (upper / lower)
