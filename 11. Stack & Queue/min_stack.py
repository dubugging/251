class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return -1
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
            self.stack.pop()
        else:
            return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else -1

    def getMin(self) -> int:
        if not self.min_stack:
            return -1
        return self.min_stack[-1]
