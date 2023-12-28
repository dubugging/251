def show(n):
    if not n:
        return
    show(n-1)
    print(n, end=' ')


show(5)
