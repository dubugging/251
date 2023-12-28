def partition(arr, pivot_index, end_index):
    boundary = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if arr[i] < arr[pivot_index]:
            boundary += 1
            arr[boundary], arr[i] = arr[i], arr[boundary]
    arr[pivot_index], arr[boundary] = arr[boundary], arr[pivot_index]
    return boundary


def quick_sort(arr, pivot_index, end_index):
    if pivot_index < end_index:
        boundary = partition(arr, pivot_index, end_index)
        quick_sort(arr, pivot_index=pivot_index, end_index=boundary - 1)
        quick_sort(arr, pivot_index=boundary + 1, end_index=end_index)
        return arr


print(quick_sort(arr=[77, 5, 89, 2, 85], pivot_index=0, end_index=4))
