def show(n):
    if not n:
        return
    print(n, end=' ')
    show(n-1)


show(5)
