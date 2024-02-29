from collections import deque


def bottom_view(root):
    mapp = {}
    q = deque([(root, 0)] if root else [])

    while q:
        node = q.popleft()
        value = node[0].value
        hd = node[1]

        mapp[hd] = value

        if node[0].left:
            q.append((node[0].left, hd-1))

        if node[0].right:
            q.append((node[0].right, hd+1))

    if mapp:
        mapp = sorted(mapp.items(), key=lambda kv: kv[0])
        return [item[1] for item in mapp]

    return []
