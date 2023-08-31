#!/usr/bin/python3
"""Defines a matrix devision function."""


def matrix_divided(matrix, div):
    """Devide all the elements of a matrix

    Args:
        matrix (list): A list of lists of intgers or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix is not a list of lists of integers and floats.
        TypeError: If the rows aren't of the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If the div is 0.
    Returns:
        A new matrix after devision
    """
    if (not isinstance(matrix, list) or
            matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(element, int) or isinstance(element, float))
                    for element in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all((len(row) == len(matrix[0])) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])