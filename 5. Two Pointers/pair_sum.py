def pairSum(arr, n, target):
    start = 0
    end = n-1
    count = 0
    while start < end:
        total = arr[start] + arr[end]
        if total == target:
            count += 1
            start += 1
            end -= 1
        elif total < target:
            start += 1
        else:
            end -= 1
    return -1 if not count else count
