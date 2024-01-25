def in_order(self):
    result = []

    def traverse(current):
        if current.left:
            traverse(current.left)
        result.append(current.value)
        if current.right:
            traverse(current.right)

    traverse(self.root)
    return result
