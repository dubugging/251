def minimumParentheses(pattern):
    stack = []
    for bra in pattern:
        if not stack:
            stack.append(bra)
        elif stack[-1] == '(':
            if bra == ')':
                stack.pop()
            else:
                stack.append(bra)
        else:
            stack.append(bra)

    return len(stack)

    
print(minimumParentheses(pattern=')(()'))