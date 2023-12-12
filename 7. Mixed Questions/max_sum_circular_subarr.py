def find_max_sum(arr):
    ans = arr[0]
    total = 0
    for num in arr:
        total += num
        if total < 0:
            total = 0
        ans = max(ans, total)
    return ans


def find_min_sum(arr):
    min_sum = arr[0]
    total = 0

    for num in arr:
        total += num
        if total > 0:
            total = 0
        min_sum = min(min_sum, total)
    return min_sum


def maxSubarraySum(arr, n):
    max_sum = find_max_sum(arr)
    min_sum = find_min_sum(arr)
    print(max_sum)
    total = sum(arr)
    return max(max_sum, total-min_sum) if max_sum > 0 else max(arr)


print(maxSubarraySum(arr=[1, -6, -7, 4], n=4))
