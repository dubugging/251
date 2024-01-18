def reverseQueue(q):
    stack = []
    while q.qsize():
        stack.append(q.get())
    while stack:
        q.put(stack.pop())
    return q
