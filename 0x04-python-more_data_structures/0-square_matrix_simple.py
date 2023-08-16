#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for row in matrix:
        newMatrix.append(list(map(lambda x: x*x, row)))
    return newMatrix
