def search(arr, item):
    if not arr:
        return False
    if arr[0] == item:
        return True
    return search(arr=arr[1:], item=item)


print(search(arr=[1, 2, 3, 4, 5, 6], item=7))
