from collections import defaultdict


def brute(arr, s):
    count = 0
    for i in range(len(arr)):
        total = arr[i]
        if total == s:
            count += 1
        for j in range(i+1, len(arr)):
            total += arr[j]
            if total == s:
                count += 1
    return count


def better(arr, s):
    total = 0
    count = 0
    mapp = {total: 1}

    for num in arr:
        total += num
        if total-s in mapp:
            count += mapp[total-s]
            mapp[total-s] += 1
        mapp[total] = 1
    return count


print(better(arr=[1, 2, 3], s=3))
