def brute(arr, k):
    count = 0
    for i in range(len(arr)):
        total = arr[i]
        if not total % k:
            count += 1
        for j in range(i+1, len(arr)):
            total += arr[j]
            if not total % k:
                count += 1
    return count


def optimal(arr, k):
    mapp = {0: 1}
    total = 0
    count = 0
    for i in range(len(arr)):
        total += arr[i]
        rem = total % k
        if rem < 0:
            rem += k
        if rem in mapp:
            count += mapp[rem]
            mapp[rem] += 1
        else:
            mapp[rem] = 1
    return count


print(optimal(arr=[5, 0, 2, 3, 1], k=5))
