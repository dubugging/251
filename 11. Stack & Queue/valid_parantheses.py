def isValidParenthesis(s: str) -> bool:
    stack = []
    mapp = {'(': 1, ')': 1, '{': 2, '}': 2, '[': 3, ']': 3}
    for bra in s:
        if not stack:
            stack.append(bra)
        elif mapp[stack[-1]] == mapp[bra]:
            stack.pop()
        else:
            stack.append(bra)
    return True if not stack else False


print(isValidParenthesis(s='[]([(]([{]]}{]{{)[}}{[{)}(}({{{])[){])({[[{[)]{)][)]{)({)[{)]{])}](]{)}][})}){({{{(){}{{(])]{{)]({{][)]{({(]{(}]{([)((}([()()[)][[}((}]}{}]]{]{{(}{)]])(((({(]}})}([{{]{]{)[]((]))[[])(]{}{)]]{[[}[][][]([(]][{[}[]}}]}{{]{}[))}}])]([))[{([(]){)}))])[]{}{[]]}})){[{]][(]}]{){[][]{[)[]}]}{{)][{[)[]{]){{(}({)))[()(}}(]}[}'))
