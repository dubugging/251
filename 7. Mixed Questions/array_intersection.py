def findArrayIntersection(arr: list, n: int, brr: list, m: int):
    i = j = 0
    ans = []
    while i < n and j < m:
        if arr[i] < brr[j]:
            i += 1
        elif arr[i] > brr[j]:
            j += 1
        else:
            ans.append(arr[i])
            i += 1
            j += 1
    return ans
