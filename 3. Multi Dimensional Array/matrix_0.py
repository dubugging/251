def setZeros(matrix):
    row = len(matrix)
    col = len(matrix[0])

    zero_rows = [0]*row
    zero_cols = [0]*col

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                zero_rows[i] = 1
                zero_cols[j] = 1

    for i in range(row):
        for j in range(col):
            if zero_rows[i] == 1 or zero_cols[j] == 1:
                matrix[i][j] = 0

    return matrix


print(setZeros(matrix=[[7, 19, 3], [4, 21, 0]]))
