#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for elements1 in matrix:
            num = 1
            length = len(elements1)

            for elements2 in elements1:
                if num == length:
                    print('{:d}'.format(elements2), end='')
                else:
                    print('{:d}'.format(elements2), end=' ')
                num += 1

            print()
