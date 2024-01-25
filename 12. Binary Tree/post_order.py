def post_order(self):
    result = []

    def traverse(current):
        if current.left:
            traverse(current.left)
        if current.right:
            traverse(current.right)
        result.append(current.value)

    traverse(self.root)
    return result
