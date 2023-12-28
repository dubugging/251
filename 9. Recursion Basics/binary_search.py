def search(arr, low, high, item):
    if low > high:
        return False

    mid = (low+high)//2

    if arr[mid] == item:
        return True
    elif arr[mid] > item:
        return search(arr=arr, low=low, high=mid-1, item=item)
    else:
        return search(arr=arr, low=mid+1, high=high, item=item)


print(search(arr=[1, 2, 9, 15, 17], low=0, high=4, item=10))
