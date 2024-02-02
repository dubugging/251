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
tree.insert(7)
tree.insert(4)
tree.insert(9)
tree.insert(1)
tree.insert(6)
tree.insert(8)

another = BST()
another.insert(7)
another.insert(4)
another.insert(9)
another.insert(1)
another.insert(6)
another.insert(8)
