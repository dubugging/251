def bubble(arr, n):
    if n <= 1:
        return arr
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return bubble(arr, n-1)


print(bubble([6, 5, 4, 1], 4))
