def findTriplet(arr, n):
    arr.sort()

    for i in range(n-1, -1, -1):
        j = 0
        k = i-1

        while j < k:
            duo_sum = arr[j] + arr[k]
            if arr[i] == duo_sum:
                return [arr[j], arr[k], arr[i]]
            elif arr[i] < duo_sum:
                k -= 1
            else:
                j += 1
    return []


print(findTriplet(arr=[1, 0, 1, 2], n=4))
