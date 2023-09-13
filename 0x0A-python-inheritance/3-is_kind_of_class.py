#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is instance or inherited instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    return issubclass(type(obj), a_class)
