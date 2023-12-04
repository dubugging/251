def maxProductCount(arr, n):
    mapp = {}

    for i in range(n):
        for j in range(i+1, n):
            a = arr[i]
            b = arr[j]
            pairproduct = a*b
            if pairproduct in mapp:
                mapp[pairproduct] += 1
            else:
                mapp[pairproduct] = 1

    maxProd = 0
    freq = 0

    for prod in mapp.keys():
        if mapp.get(prod) >= freq:
            if mapp.get(prod) == freq:
                maxProd = min(maxProd, prod)
            else:
                maxProd = prod

            freq = mapp.get(prod)

    lst = []

    if (mapp.get(maxProd) == None or mapp.get(maxProd) == 1):
        lst.append(0)
        lst.append(0)
        return lst
    else:
        allCombinations = ((freq * (freq - 1))) // 2
        lst.append(maxProd)
        lst.append(allCombinations)
        return lst
