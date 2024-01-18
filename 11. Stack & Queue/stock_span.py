def findSpans(price):
    stack = []
    for i in range(len(price)):
        item = price[i]
        while stack and stack[-1][0] < item:
            stack.pop()
        if not stack:
            price[i] = i+1
        else:
            price[i] = i-stack[-1][1]
        stack.append((item, i))
    return price


print(findSpans(price=[18, 12, 13, 14, 11, 16]))
