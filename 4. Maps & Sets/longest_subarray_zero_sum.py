def brute(arr):
    distance = 0
    n = len(arr)

    for i in range(n):
        total = arr[i]
        if not total:
            distance = i+1
        for j in range(i+1, n):
            total += arr[j]
            if not total:
                distance = max(distance, j-i+1)

    return distance


def optimal(arr):
    mapp = {}
    presum = 0
    result = 0

    for i in range(len(arr)):
        presum += arr[i]
        if not presum:
            result = i+1
        elif presum in mapp:
            result = max(result, i-mapp[presum])
        else:
            mapp[presum] = i

    return result


print(optimal(arr=[1, -1, 2, -2]))
