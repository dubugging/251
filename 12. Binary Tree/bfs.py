from collections import deque


def bfs(root):
    ans = []
    queue = deque([root] if root else [])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ans.append(level)

    return ans
