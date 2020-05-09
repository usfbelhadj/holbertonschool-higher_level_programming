#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    mat = []
    for i in matrix:
        mat.append(list(map(lambda x: x*x, i)))
    return mat
