#!/usr/bin/python3
def common_elements(set_1, set_2):
    return filter(lambda number: True if number in set_2 else False, set_1)
