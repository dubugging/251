def brute(arr, n, target) -> [[int]]:
    ans = set()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == target:
                    temp = sorted([arr[i], arr[j], arr[k]])
                    ans.add(tuple(temp))
    return [list(item) for item in ans]


def better(arr, n, target) -> [[int]]:
    ans = set()
    for i in range(n):
        st = set()
        for j in range(i+1, n):
            find = target - (arr[i]+arr[j])
            if find not in st:
                st.add(arr[j])
            else:
                temp = sorted([arr[i], arr[j], find])
                ans.add(tuple(temp))
    return [list(item) for item in ans]


def optimal(arr, n, target) -> [[int]]:
    arr.sort()
    ans = []
    for i in range(n):
        if i > 0 and arr[i-1] == arr[i]:
            continue
        j, k = i+1, n-1
        while j < k:
            total = arr[i] + arr[j] + arr[k]
            if total == target:
                ans.append([arr[i], arr[j], arr[k]])
                j += 1
                k -= 1
                while j < k and arr[j] == arr[j-1]:
                    j += 1
                while j < k and arr[k] == arr[k+1]:
                    k -= 1
            elif total < target:
                j += 1
            else:
                k -= 1
    return ans


print(better(n=5, arr=[-1, -1, 2, 0, 1], target=2))
