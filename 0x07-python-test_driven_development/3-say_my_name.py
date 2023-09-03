#!/usr/bin/python3
"""Defines a name printing function."""


def say_my_name(first_name, last_name=""):
    """Print a given name

    Args:
        first_name (string): The first name.
        last_name (string): The last name.
    Raises:
        TypeError: If first_name or last_name aren't strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
