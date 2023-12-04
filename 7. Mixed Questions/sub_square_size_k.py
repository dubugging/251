def sumOfKxKMatrices(arr: list, k: int):
    n = len(arr)
    ans = [[0 for i in range(n-k+1)] for j in range(n-k+1)]

    for i in range(n-k+1):
        for j in range(n-k+1):
            sm = 0
            for x in range(k):
                for y in range(k):
                    sm += arr[x + i][y + j]
            ans[i][j] = sm
    return ans


print(sumOfKxKMatrices(arr=[[8, 1, 3], [2, 9, 3], [0, 3, 5]], k=2))
