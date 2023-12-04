def find(arr, n, item):
    for i in range(n):
        if arr[i] == item:
            return True
    return False


def brute(arr, n):
    ans = 0
    for i in range(n):
        item = arr[i]
        count = 1
        while find(arr, n, item+1):
            count += 1
            item += 1
        ans = max(ans, count)
    return ans


def better(arr, n):
    arr.sort()
    count = 1
    ans = 1
    for i in range(n-1):
        if arr[i+1] - arr[i] == 1:
            count += 1
        elif arr[i+1] - arr[i] > 1:
            count = 1
        ans = max(ans, count)
    return ans


print(better(
    arr=[0, 1, 1, 2], n=4))
