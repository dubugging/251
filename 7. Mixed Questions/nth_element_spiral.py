def findKthElement(matrix, k):
    top, left = 0, 0
    right, bottom = len(matrix[0])-1, len(matrix)-1
    count = 0

    while top <= bottom and left <= right:
        for index in range(left, right+1):
            count += 1
            if count == k:
                return matrix[top][index]
        top += 1

        for index in range(top, bottom+1):
            count += 1
            if count == k:
                return matrix[index][right]
        right -= 1

        if top <= bottom:
            for index in range(right, left-1, -1):
                count += 1
                if count == k:
                    return matrix[bottom][index]
        bottom -= 1

        for index in range(bottom, top-1, -1):
            count += 1
            if count == k:
                return matrix[index][left]
        left += 1


print(findKthElement(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [
      9, 10, 11, 12], [13, 14, 15, 16]], k=10))
