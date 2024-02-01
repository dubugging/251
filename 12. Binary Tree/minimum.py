def minimum(root):
    if not root:
        return float('inf')
    if not root.left and not root.right:
        return root.value
    return min(minimum(root.left), minimum(root.right), root.value)
