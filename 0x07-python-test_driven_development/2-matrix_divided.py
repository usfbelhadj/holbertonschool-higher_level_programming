#!/usr/bin/python3


def matrix_divided(matrix, div):
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        print(row)
        if len(row) != len(matrix[0]):
            raise TypeError(
                     "Each row of the matrix must have the same size"
                     )
        for i in row:
            if type(matrix) is not list and type(i) not in (int, float):
                raise TypeError(
                 "matrix must be a matrix (list of lists) of integers/floats"
                 )
    return list(map(lambda y: list(map(lambda x: round(x/div,
                                       2), y)), matrix))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
