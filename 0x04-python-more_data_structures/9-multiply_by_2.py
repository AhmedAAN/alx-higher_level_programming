#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newDictionary = a_dictionary.copy()
    dictionaryKeys = list(a_dictionary.keys())
    for key in dictionaryKeys:
        newDictionary[key] *= 2
    return newDictionary
