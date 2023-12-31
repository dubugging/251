def pushZerosAtEnd(arr):
    n = len(arr)
    zero_index = 0
    for i in range(n):
        if arr[i] == 0:
            if i > zero_index:
                continue
            zero_index = i
        else:
            if i > zero_index:
                arr[zero_index], arr[i] = arr[i], arr[zero_index]
            zero_index += 1
    return arr


print(pushZerosAtEnd(arr=[2, 0, 4, 1, 3, 0, 28]))
print(pushZerosAtEnd(arr=[0, 0, 4, 1, 3, 0, 28]))
