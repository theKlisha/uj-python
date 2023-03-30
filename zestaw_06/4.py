#!/bin/python3

import re

if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    matrix = []

    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)

    a = [matrix[i][j] for j in range(m) for i in range(n)]
    s = ''.join(a)
    e = r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])'
    print(re.sub(e ,' ', s))
