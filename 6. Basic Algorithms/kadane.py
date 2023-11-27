def maxSubarraySum(arr):
    ans = arr[0]
    total = 0
    for num in arr:
        total += num
        if total < 0:
            total = 0
        ans = max(ans, total)
    return ans


print(maxSubarraySum(arr=[-30]))
