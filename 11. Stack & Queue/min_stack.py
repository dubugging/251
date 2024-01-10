class minStack:
    def __init__(self):
        self.stack = []

    # Function to add another element equal to num at the top of stack.
    def push(self, num: int) -> None:
        self.stack.append(num)

    # Function to remove the top element of the stack.
    def pop(self) -> int:
        return self.stack.pop() if self.stack else -1

    # Function to return the top element of stack if it is present. Otherwise return -1.
    def top(self) -> int:
        return self.stack[-1] if self.stack else -1

    # Function to return minimum element of stack if it is present. Otherwise return -1.
    def getMin(self) -> int:
        mini = -1
        for i in range(len(self.stack)):
            if self.stack[i] < mini:
                mini = self.stack[i]
        return mini
