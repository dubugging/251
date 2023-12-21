def is_possible(stalls, gap, cows):
    count_cows = 1
    last = stalls[0]
    for i in range(1, len(stalls)):
        if stalls[i] - last >= gap:
            count_cows += 1
            last = stalls[i]
        if count_cows >= cows:
            return True
    return False


def aggressiveCows(stalls, k):
    stalls.sort()
    low, high = 1, stalls[-1]-stalls[0]
    while low <= high:
        mid = (low+high)//2
        if is_possible(stalls, mid, k):
            low = mid+1
        else:
            high = mid-1
    return high


print(aggressiveCows(stalls=[0, 3, 4, 7, 10, 9], k=4))
