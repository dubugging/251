def minimum(self):
    def traverse(current):
        if not current:
            return float('inf')
        if not current.left and not current.right:
            return current.value
        return min(traverse(current.left), traverse(current.right), current.value)

    return traverse(self.root)
