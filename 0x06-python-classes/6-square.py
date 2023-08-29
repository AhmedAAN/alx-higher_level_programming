#!/usr/bin/python3

"""Define Class Square."""


class Square:
    """Represents a Square."""

    def __init__(self, size = 0, position=(0, 0)):
        """Initialize a Square.
        
        Args:
            size (int): The size of the new Square
        """
        self.__size = size
        self.__position = position
    
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

    @property
    def position(self):
        """Get/set the position of the current square"""
        return (self.__position)
    
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num > 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the current Square"""
        return (slef.__size ** 2)
    
    def my_print(self):
        """Prints the square with the # character."""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            for y in range(self.__position[0]):
                print(" ", end = "")
            for x in range(self.__size):
                print("#", end = "")
            print("")
        