#!/usr/bin/python3
"""Defines a square printing function."""


def print_square(size):
    """Print a square with the character #

    Args:
        size (int): The size length of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than zero.
        TypeError: If size is a float and is less than 0.
    """
    if (isinstance(size, float) and int(size) < 0):
        raise TypeError("size must be an integer")
    if int(size) < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    for row in range(size):
        for element in range(size):
            print("#", end = "")
        print("")
