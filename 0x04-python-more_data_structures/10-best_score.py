#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    values = list(a_dictionary.values())
    keys = list(a_dictionary.keys())
    maxValueIndex = values.index(max(values))
    return keys[maxValueIndex]
