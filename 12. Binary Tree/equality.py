def equals(root1, root2):
    if not root1 and not root2:
        return True
    if root1 and root2:
        if root1.value != root2.value:
            return False
        return equals(root1.left, root2.left) and equals(root1.right, root2.right)
    return False
