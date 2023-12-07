def brute(arr, target):
    n = len(arr)
    ans = set()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if arr[i]+arr[j]+arr[k]+arr[l] == target:
                        temp = sorted([arr[i], arr[j], arr[k], arr[l]])
                        ans.add(tuple(temp))
    return [list(item) for item in ans]


def better(arr, target):
    n = len(arr)
    ans = set()
    for i in range(n):
        for j in range(i+1, n):
            st = set()
            for k in range(j+1, n):
                find = target - arr[i] - arr[j] - arr[k]
                if find in st:
                    temp = sorted([arr[i], arr[j], arr[k], find])
                    ans.add(tuple(temp))
                st.add(arr[k])

    return [list(item) for item in ans]


def optimal(arr, target):
    n = len(arr)
    arr.sort()
    ans = []
    for i in range(n):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1, n):
            if j > 1 and arr[j] == arr[j-1]:
                continue
            k, l = j+1, n-1
            while k < l:
                total = arr[i] + arr[j] + arr[k] + arr[l]
                if total == target:
                    temp = sorted([arr[i], arr[j], arr[k], arr[l]])
                    ans.append(temp)
                    k += 1
                    l -= 1
                    while k < l and arr[k] == arr[k-1]:
                        k += 1
                    while k < l and arr[l] == arr[l+1]:
                        l -= 1
                elif total < target:
                    k += 1
                else:
                    l -= 1
    return ans


print(optimal(arr=[1, 3, 3, 10, 2], target=9))
