class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
            return True
        curr = self.root
        while True:
            if value == curr.value:
                return False
            elif value < curr.value:
                if not curr.left:
                    curr.left = node
                    return True
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = node
                    return True
                curr = curr.right

    def contains(self, value):
        curr = self.root
        while curr:
            if value == curr.value:
                return True
            elif value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return False

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

    def height(self):
        def traverse(current):
            if not current:
                return -1
            if not current.left and not current.right:
                return 0
            return 1 + max(traverse(current.left), traverse(current.right))

        return traverse(self.root)

    def minimum(self):
        def traverse(current):
            if not current:
                return 1
            if not current.left and not current.right:
                return current.value
            return min(traverse(current.left), traverse(current.right), current.value)

        return traverse(self.root)


tree = BST()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)

print(tree.pre_order())
print(tree.in_order())
print(tree.post_order())
print(tree.height())
print(tree.minimum())
