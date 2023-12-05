#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for s_matrix in matrix:
        if len(s_matrix) == 0:
            print()
        for item in range(len(s_matrix)):
            print("{:d}".format(s_matrix[item]), end="\n"
                  if item is len(s_matrix) - 1 else " ")
