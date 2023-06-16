#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for i in new_matrix:
        i = list(map(lambda x: x ** 2, i))
    return (new_matrix)
