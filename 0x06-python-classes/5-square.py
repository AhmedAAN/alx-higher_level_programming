#!/usr/bin/python3

"""Define Class Square."""


class Square:
    """Represents a Square."""

    def __init__(self, size=0):
        """Initialize a Square.

        Args:
            size (int): The size of the new Square
        """
        self.size = size

    @property
    def size(self):
        """Get/set the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the current Square"""
        return (slef.__size ** 2)

    def my_print(self):
        """Prints the square with the # character."""
        for i in range(self.__size):
            for x in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
