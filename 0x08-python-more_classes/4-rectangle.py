#!/usr/bin/python3

"""Define a class Rectangle ."""


class Rectangle:
    """Represent a Rectangle ."""

    def __init__(self, width=0, height=0):
        """Intialize a new rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The length of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/sets width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get/sets height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if (self.__width == 0 or self.__height == 0):
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """Represents the rectangle with the # character."""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            if i != 0:
                rect.append("\n")
            [rect.append("#") for j in range(self.__width)]
        return ("".join(rect))

    def __repr__(self):
        """Retrun the string representation of the rectangle."""
        return ("Rectangle({}, {})".format(self.__width, self.__height))
