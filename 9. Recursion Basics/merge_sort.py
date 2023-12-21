def merge(left, right):
    ans = []
    n1, n2 = len(left), len(right)
    i, j = 0, 0
    while i < n1 and j < n2:
        if left[i] < right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1
    if i < n1:
        ans += left[i:]
    if j < n2:
        ans += right[j:]
    return ans


def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    return merge(mergeSort(left), mergeSort(right))


print(mergeSort(arr=[7, 8, 3, 2, 1]))
