def height(root):
    if not root:
        return -1
    if not root.left and not root.right:
        return 0
    return 1 + max(height(root.left), height(root.right))
