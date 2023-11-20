def isMatrixSymmetric(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]: return False
    return True


print(isMatrixSymmetric(matrix=[[1,2], [2,1]]))