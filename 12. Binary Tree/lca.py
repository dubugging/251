def lowestCommonAncestor(root, p, q):
    if not root or root.val == p.val or root.val == q.val:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if not left:
        return right
    elif not right:
        return left
    else:
        return root
