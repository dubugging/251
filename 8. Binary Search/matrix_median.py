def get_min(matrix):
    minimum = matrix[0][0]
    for i in range(1, len(matrix)):
        minimum = min(minimum, matrix[i][0])
    return minimum


def get_max(matrix):
    maximum = matrix[0][len(matrix[0])-1]
    for i in range(1, len(matrix)):
        maximum = max(maximum, matrix[i][len(matrix[0])-1])
    return maximum


def upper_bound(arr, x, n):
    low = 0
    high = n-1
    ans = n
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] > x:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans


def count_smaller_equal(matrix, n, m, x):
    count = 0
    for i in range(n):
        count += upper_bound(matrix[i], x, m)
    return count


def getMedian(matrix):
    low = get_min(matrix)
    high = get_max(matrix)
    n = len(matrix)
    m = len(matrix[0])
    req = (n*m) // 2
    while low <= high:
        mid = (low+high) // 2
        small_equal = count_smaller_equal(matrix, n, m, mid)
        if small_equal <= req:
            low = mid+1
        else:
            high = mid-1
    return low


print(getMedian(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
