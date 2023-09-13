#!/usr/bin/python3
"""Defines an inherited list class MyList."""

class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """  Returns the list of available attributes and methods of an object."""
        print(sorted(self))