class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diameterOfBinaryTree(root: TreeNode) -> int:
    if not root:
        return 0

    left_diameter = diameterOfBinaryTree(root.left)
    right_diameter = diameterOfBinaryTree(root.right)

    current = height(root.left) + height(root.right)

    return max(current, max(left_diameter, right_diameter))


def height(current):
    if not current:
        return 0
    return 1 + max(height(current.left), height(current.right))
