def left_traverse(root, ans):
    if not root or (not root.left and not root.right):
        return
    ans.append(root.value)
    if root.left:
        left_traverse(root.left, ans)
    else:
        left_traverse(root.right, ans)


def leaf_traverse(root, ans):
    if not root:
        return
    if not root.left and not root.right:
        ans.append(root.value)
    leaf_traverse(root.left, ans)
    leaf_traverse(root.right, ans)


def right_traverse(root, ans):
    if not root or (not root.left and not root.right):
        return
    if root.right:
        right_traverse(root.right, ans)
    else:
        right_traverse(root.left, ans)
    ans.append(root.value)


def traverseBoundary(root):
    ans = [root.value] if root else []
    left_traverse(root.left, ans)
    leaf_traverse(root, ans)
    right_traverse(root.right, ans)
    return ans
