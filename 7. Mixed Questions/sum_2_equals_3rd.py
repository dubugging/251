def findTriplet(arr, n):
    count = 0
    arr.sort()

    for i in range(n-1, -1, -1):
        j = 0
        k = i-1

        while j < k:
            if arr[i] == arr[j] + arr[k]:
                count += 1
                break
            elif arr[i] < arr[j] + arr[k]:
                k -= 1
            else:
                j -= 1
    return count


print(findTriplet(arr=[1, 0, 1], n=3))
