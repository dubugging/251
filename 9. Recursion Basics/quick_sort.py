def partition(arr, pivot_index, end_index):
    boundary = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if arr[i] < arr[pivot_index]:
            boundary += 1
            arr[boundary], arr[i] = arr[i], arr[boundary]
    arr[pivot_index], arr[boundary] = arr[boundary], arr[pivot_index]
    return boundary


def quickSort(arr, start, end):
    if start < end:
        boundary = partition(arr, pivot_index=start, end_index=end)
        quickSort(arr, start=start, end=boundary-1)
        quickSort(arr, start=boundary+1, end=end)
    return arr


print(quickSort([15, 6, 3, 1, 22, 10, 13], start=0, end=6))
