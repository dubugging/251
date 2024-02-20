from collections import deque


def bfs(root):
    ans = []
    q = deque([root] if root else [])

    while q:
        node = q.popleft()
        ans.append(node.value)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return ans
