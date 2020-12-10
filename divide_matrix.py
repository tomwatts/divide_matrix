# Given a square matrix and a size such that size evenly divides len(matrix),
# divides the matrix into submatrices of size x size.
def divide_matrix(matrix, size):
    submatrices = list()

    for i in range(0, len(matrix), size):
        rows = matrix[i:i + size]
        for j in range(0, len(matrix), size):
            submatrix = [r[j:j + size] for r in rows]
            submatrices.append(submatrix)

    return submatrices


matrix = [[0,  1,  2,  3],
          [4,  5,  6,  7],
          [8,  9,  10, 11],
          [12, 13, 14, 15]]
assert divide_matrix(matrix, 2) == [[[0,  1],  [4,  5]],
                                    [[2,  3],  [6,  7]],
                                    [[8,  9],  [12, 13]],
                                    [[10, 11], [14, 15]]]


matrix = [[0,  1,  2,  3,  4,  5],
          [6,  7,  8,  9,  10, 11],
          [12, 13, 14, 15, 16, 17],
          [18, 19, 20, 21, 22, 23],
          [24, 25, 26, 27, 28, 29],
          [30, 31, 32, 33, 34, 35]]
assert divide_matrix(matrix, 3) == [[[0,  1,  2],  [6,  7,  8],  [12, 13, 14]],
                                    [[3,  4,  5],  [9,  10, 11], [15, 16, 17]],
                                    [[18, 19, 20], [24, 25, 26], [30, 31, 32]],
                                    [[21, 22, 23], [27, 28, 29], [33, 34, 35]]]
