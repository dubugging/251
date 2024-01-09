class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def push(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def pop(self):
        if self.size:
            curr = self.head
            self.size -= 1
            while curr.next:
                previous = curr
                curr = curr.next
            previous.next = None
            self.tail = previous

    def getTop(self):
        return self.tail.value
