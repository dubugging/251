def spiralPrint(mat, nRows, mCols):
    left = 0
    right = mCols - 1
    top = 0
    bottom = nRows - 1

    while top <= bottom and left <= right:
        for i in range(left, right+1):
            print(mat[top][i], end=' ')

        top += 1

        for i in range(top, bottom+1):
            print(mat[i][right], end=' ')

        right -= 1

        if top <= bottom:
            for i in range(right, left-1, -1):
                print(mat[bottom][i], end=' ')

            bottom -= 1

        for i in range(bottom, top-1, -1):
            print(mat[i][left], end=' ')

        left += 1


spiralPrint(mat=[[1,2,3], [4,5,6], [7,8,9]], nRows=3, mCols=3)
