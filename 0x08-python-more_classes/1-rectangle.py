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
        return this.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        
        if value < 0:
            raise ValueError("width must be >= 0")
        
        this.__width = value

    @property
    def height(self):
        """Get/sets height of the rectangle."""
        return this.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        
        if value < 0:
            raise ValueError("height must be >= 0")
        
        this.__height = value
