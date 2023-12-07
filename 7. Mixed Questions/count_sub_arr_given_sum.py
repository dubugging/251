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
    pre_sum, count = 0, 0
    mapp = defaultdict(int)
    mapp[0] = 1
    for num in arr:
        pre_sum += num
        remove = pre_sum - s
        count += mapp[remove]
        mapp[pre_sum] += 1
    return count


print(better(arr=[1, 2, 3], s=3))
