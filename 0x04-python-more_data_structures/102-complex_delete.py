#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = a_dictionary.copy()
    values = list(new.values())
    keys = list(new.keys())
    while value in values:
        index = values.index(value)
        key = keys[index]
        keys.pop(index)
        values.pop(index)
        del new[key]
    return (new)
