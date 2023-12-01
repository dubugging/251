def my_reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


def rotateMatRight(mat, n, m, k):
    k %= m
    for i in range(n):
        mat[i] = my_reverse(mat[i], start=0, end=m-k-1)
        mat[i] = my_reverse(mat[i], start=m-k, end=m-1)
        mat[i] = my_reverse(mat[i], start=0, end=m-1)
    return mat


print(rotateMatRight(
    mat=[[1, 2, 3], [4, 5, 6]], n=2, m=3, k=2))
