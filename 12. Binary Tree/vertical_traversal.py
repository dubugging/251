from collections import deque


def verticalOrderTraversal(root):
    mapp = {}
    q = deque([(root, 0)] if root else [])
    ans = []

    while q:
        node = q.popleft()
        value = node[0].value
        hd = node[1]

        if hd not in mapp:
            mapp[hd] = [value]
        else:
            mapp[hd] += [value]

        if node[0].left:
            q.append((node[0].left, hd-1))

        if node[0].right:
            q.append((node[0].right, hd+1))

    if mapp:
        mapp = sorted(mapp.items(), key=lambda kv: kv[0])
        for item in mapp:
            ans += item[1]

    return ans
