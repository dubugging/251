def validate(root, mini, maxi):
    if not root:
        return True
    if not mini < root.value < maxi:
        return False
    return validate(root.left, mini, root.value-1) and \
        validate(root.right, root.value+1, maxi)
