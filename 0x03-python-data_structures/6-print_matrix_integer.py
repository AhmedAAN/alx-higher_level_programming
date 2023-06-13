#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(0, len(matrix)):
        for point in range(0, len(matrix[row])):
            if point != 0:
                print(end=" ")
            print("{:d}".format(matrix[row][point]), end="")
        print("")
