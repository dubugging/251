def brute(arr, n):
    sets = set()
    for item in arr:
        if item > 0:
            sets.add(item)

    for ans in range(1, n+2):
        if ans not in sets:
            return ans


def optimal(arr, n):
    i = 0
    while i < n:
        element = arr[i]
        chair = element - 1

        if 1 <= element <= n and arr[chair] != element:
            arr[i], arr[chair] = arr[chair], arr[i]
        else:
            i += 1 ## increment only if item is -ve and beyond length of array and it is placed in correct index

    for i in range(n):
        if i+1 != arr[i]:
            return i+1

    return n+1


print(optimal(arr=[5,4,3,2,1], n=5))
print(brute(arr=[1,2,0], n=3))