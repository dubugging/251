def solution(string, temp, index):
    if len(string) == index:
        print(temp, end=' ')
        return
    # take
    solution(string, temp+string[index], index+1)
    # not take
    solution(string, temp, index+1)


solution(string='abc', temp='', index=0)
