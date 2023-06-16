#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    values = list(a_dictionary.values())
    index = values.index(max(values))
    keys = list(a_dictionary.keys())
    return (keys[index])
