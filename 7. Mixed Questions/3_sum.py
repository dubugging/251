def brute(n: int, arr: [int]) -> [[int]]:
    ans = set()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if not arr[i] + arr[j] + arr[k]:
                    temp = [arr[i], arr[j], arr[k]]
                    temp.sort()
                    ans.add(tuple(temp))
    return list(ans)


def better(n: int, arr: [int]) -> [[int]]:
    ans = set()
    for i in range(n):
        st = set()
        for j in range(i+1, n):
            find = -(arr[i]+arr[j])
            if find not in st:
                st.add(arr[j])
            elif find in st:
                temp = [arr[i], find, arr[j]]
                temp.sort()
                ans.add(tuple(temp))
    return [list(item) for item in ans]


def optimal(n: int, arr: [int]) -> [[int]]:
    pass


print(better(n=5, arr=[-1, -1, 2, 0, 1]))
