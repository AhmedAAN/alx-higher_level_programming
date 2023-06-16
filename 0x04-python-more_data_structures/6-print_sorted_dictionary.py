#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = list(a_dictionary.keys())
    new = sorted(new)
    for i in new:
        print ("{}: {}".format(i, a_dictionary[i]))
