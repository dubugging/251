class Stack:
    def __init__(self):
        self.que1 = []
        self.que2 = []

    def getSize(self) -> int:
        return len(self.que1)

    def isEmpty(self) -> bool:
        return len(self.que1) == 0

    def push(self, element: int) -> None:
        if not self.que1:
            self.que1.append(element)
        else:
            self.que2 = self.que1[:]
            self.que1.clear()
            self.que1.append(element)
            self.que1 += self.que2[:]
            self.que2.clear()

    def pop(self) -> int:
        return self.que1.pop(0) if self.que1 else -1

    def top(self) -> int:
        return self.que1[-1] if self.que1 else -1
