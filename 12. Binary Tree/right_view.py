from collections import deque


def right_view(root):
    ans = []
    q = deque([root] if root else [])

    while q:
        level = 0

        for _ in range(len(q)):
            node = q.popleft()
            level = node.value
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level)

    return ans
