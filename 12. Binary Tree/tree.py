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


tree = BST()
tree.insert(2)
tree.insert(3)
tree.insert(1)

print(tree.contains(1))
