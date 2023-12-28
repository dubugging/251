def is_sorted(arr):
    if len(arr) <= 1:
        return True
    if arr[0] > arr[1]:
        return False
    return is_sorted(arr=arr[1:])


print(is_sorted(arr=[1, 2, 3, 3, 5, 5, -5]))
