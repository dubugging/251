class Stack:
    def __init__(self, n: int):
        self.arr = []
        self.size = n

    def push(self, num: int):
        if not self.isFull():
            self.arr.append(num)

    def pop(self) -> int:
        return self.arr.pop() if self.arr else -1

    def top(self) -> int:
        return self.arr[-1] if self.arr else -1

    def isEmpty(self) -> int:
        return not self.arr

    def isFull(self) -> int:
        return len(self.arr) >= self.size
