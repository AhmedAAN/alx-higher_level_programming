#!/usr/bin/python3

"""Define a class Rectangle ."""


class Rectangle:
    """Represent a Rectangle .

    Attributes:
        number_of_instances (int): The number of rectangle objects.
        print_symbol (char): The charecter to represent the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Intialize a new rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The length of the rectangle.
        """
        type(self).number_of_instances += 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the rectangle with greater area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        rect_1_area = rect_1.area()
        rect_2_area = rect_2.area()

        if rect_1_area >= rect_2_area:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new rectangle with equal width and height.

        Args:
            size (int): The width and heigh of the new rectangle.
        """
        return (cls(size, size))

    def __str__(self):
        """Represents the rectangle with the # character."""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            if i != 0:
                rect.append("\n")
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
        return ("".join(rect))

    def __repr__(self):
        """Retrun the string representation of the rectangle."""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Deletes the rectangle and prints a message"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
