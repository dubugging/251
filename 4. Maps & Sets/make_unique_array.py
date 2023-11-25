def minElementsToRemove(arr):
    count = 0
    arr.sort()
    
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            count += 1

    return count
