class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root, ans):
    if not root:
        return 0
    lh = height(root.left, ans)
    rh = height(root.right, ans)
    ans[0] = max(ans[0], lh+rh)
    return 1 + max(lh, rh)


def diameterOfBinaryTree(root: TreeNode) -> int:
    ans = [0]
    height(root, ans)
    return ans[0]
