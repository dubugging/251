def nextGreater(arr, n):
    stack = []
    for i in range(n-1, -1, -1):
        item = arr[i]
        while stack and stack[-1] <= item:
            stack.pop()
        if not stack:
            arr[i] = -1
        else:
            arr[i] = stack[-1]
        stack.append(item)
    return arr


print(nextGreater(arr=[3, 9, 2, 7, 7], n=5))
