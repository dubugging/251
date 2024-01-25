def pre_order(self):
    result = []

    def traverse(current):
        result.append(current.value)
        if current.left:
            traverse(current.left)
        if current.right:
            traverse(current.right)

    traverse(self.root)
    return result
