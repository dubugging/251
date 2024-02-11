from collections import deque


def left_view(root):
    ans = []
    q = deque([root] if root else [])

    while q:
        level = 0
        for _ in range(len(q)):
            node = q.popleft()
            if not level:
                level = node.value
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level)

    return ans
