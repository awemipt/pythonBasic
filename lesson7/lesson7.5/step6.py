def verify(matrix):
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            if not is_isolate(matrix, i, j):
                return False
    return True


def is_isolate(matrix, i, j):
    return matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1] > 1
