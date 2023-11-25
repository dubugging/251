def count_left(i, j, mat):
    if j == 0: return 0
    elif mat[i][j-1] == 1: return 1
    return 0


def count_down(i, j, mat):
    if i == len(mat)-1: return 0
    elif mat[i+1][j] == 1: return 1
    return 0


def count_right(i, j, mat):
    if j == len(mat[0])-1: return 0
    elif mat[i][j+1] == 1: return 1
    return 0


def count_up(i, j, mat):
    if i == 0: return 0
    elif mat[i-1][j] == 1: return 1
    return 0


def count_all(i, j, mat):
    return count_left(i, j, mat) + count_down(i, j, mat) + \
    	count_right(i, j, mat) + count_up(i, j, mat)


def coverageOfMatrix(mat):
    row = len(mat)
    col = len(mat[0])
    count = 0

    for i in range(row):
        for j in range(col):
            if mat[i][j] == 0:
                count += count_all(i=i, j=j, mat=mat)
    return count


print(coverageOfMatrix(mat=[[0, 0, 1], [0, 1, 0], [0,1,1]]))
