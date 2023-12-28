def solution(arr, temp, index):
    if len(arr) == index:
        if temp:
            print(temp)
        return
    # take
    solution(arr, temp=temp+[arr[index]], index=index+1)
    # not take
    solution(arr, temp=temp, index=index+1)


solution(arr=[1, 2, 3], temp=[], index=0)
