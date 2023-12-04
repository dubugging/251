def missingAndRepeating(arr, n):
    mapp = {}
    missing = 0
    repeating = 0
    for key in arr:
        if key not in mapp:
            mapp[key] = 1
        else:
            mapp[key] += 1

    for i in range(1, n+1):
        if i not in mapp:
            missing = i
        elif mapp[i] == 2:
            repeating = i

    return [missing, repeating]


print(missingAndRepeating(arr=[5, 4, 2, 4, 1], n=5))
