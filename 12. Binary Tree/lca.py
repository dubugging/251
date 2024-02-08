def lowestCommonAncestor(root, p, q):
    if not root or root.val == p.val or root.val == q.val:
        return root

    left = lowestCommonAncestor(root=root.left, p=p, q=q)
    right = lowestCommonAncestor(root=root.right, p=p, q=q)

    if not left:
        return right
    elif not right:
        return left
    else:
        return root
