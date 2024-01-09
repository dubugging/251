class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    # Define data members and __init__()

    '''----------------- Public Functions of Queue -----------------'''

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        if not self.size:
            return -1
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def front(self):
        return self.head.data if self.size else -1
