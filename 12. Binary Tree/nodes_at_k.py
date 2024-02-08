def nodes_at_k(root, k):
    nodes = []

    def traverse(root, k):
        if not k:
            nodes.append(root.value)
        if root.left:
            traverse(root=root.left, k=k-1)
        if root.right:
            traverse(root=root.right, k=k-1)
    traverse(root=root, k=k)
    return nodes
