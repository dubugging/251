def approach_one(arr):
    mapp = {}
    ans = []
    for num in arr:
        if num not in mapp:
            mapp[num] = 1
        else:
            mapp[num] += 1

    for key in mapp:
        if mapp[key] > len(arr)//3:
            ans.append(key)
    return ans


def approach_two(arr):
    n = len(arr)
    first = second = 0
    first_count = second_count = 0
    ans = []

    for i in range(n):
        if arr[i] == first:
            first_count += 1
        elif arr[i] == second:
            second_count += 1
        elif first_count == 0:
            first = arr[i]
            first_count = 1
        elif second_count == 0:
            second = arr[i]
            second_count = 1
        else:
            first_count -= 1
            second_count -= 1

    if arr.count(first) > n//3:
        ans.append(first)
    if arr.count(second) > n//3:
        ans.append(second)

    return ans


print(approach_two(arr=[1, 2, 3, 4, 4, 4]))
