def search(arr, target):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[low] <= arr[mid]:
            if arr[low] <= target <= arr[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if arr[mid] <= target <= arr[high]:
                low = mid+1
            else:
                high = mid-1
    return -1


print(search(arr=[5, 6, 7, 1, 2, 3, 4, 5], target=2))
