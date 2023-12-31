def singleNonDuplicate(arr):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)
        if mid % 2 == 0:
            if arr[mid-1] == arr[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if arr[mid] == arr[mid-1]:
                low = mid+1
            else:
                high = mid-1
    return arr[high]


print(singleNonDuplicate(arr=[1, 1, 5, 5, 10]))
