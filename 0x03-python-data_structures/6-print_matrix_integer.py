#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        first = 1
        for number in row:
            if first == 1:
                first = 0
            else:
                print("",end = " ")
            print("{}".format(number),end = "")
        print()
