def sum_of_arr(arr):
    if not arr:
        return 0
    return arr[0] + sum_of_arr(arr=arr[1:])


print(sum_of_arr(arr=[1, 2, 3, 4]))
