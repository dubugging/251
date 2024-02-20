def left_traverse(root, ans):
    if not root or (not root.left and not root.right):
        return
    ans.append(root.value)
    if root.left:
        left_traverse(root=root.left, ans=ans)
    if root.right:
        left_traverse(root=root.right, ans=ans)


def leaf_traverse(root, ans):
    if not root:
        return
    if not root.left and not root.right:
        ans.append(root.value)
        return
    leaf_traverse(root=root.left, ans=ans)
    leaf_traverse(root=root.right, ans=ans)


def right_traverse(root, ans):
    if not root or (not root.left and not root.right):
        return
    if root.right:
        right_traverse(root=root.right, ans=ans)
    if root.left:
        right_traverse(root=root.left, ans=ans)
    ans.append(root.value)


def traverseBoundary(root):
    ans = [root.value] if root else []
    left_traverse(root=root.left, ans=ans)
    leaf_traverse(root=root, ans=ans)
    right_traverse(root=root.right, ans=ans)
    return ans
