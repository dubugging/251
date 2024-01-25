def height(self):
    def traverse(current):
        if not current:
            return -1
        if not current.left and not current.right:
            return 0
        return 1 + max(traverse(current.left), traverse(current.right))

    return traverse(self.root)
