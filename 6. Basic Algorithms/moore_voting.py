def findMajorityElement(arr, n):
    count = 1
    item = arr[0]
    for i in range(1, n):
        if not count:
            count = 1
            item = arr[i]
        elif item == arr[i]:
            count += 1
        else:
            count -= 1
    return item if arr.count(item) > n//2 else -1


print(findMajorityElement(arr=[5, 2, 2, 0, 2], n=5))
