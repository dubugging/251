class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def addNodes(head, n, m):
    curr = head

    while True:
        for _ in range(m):
            if curr:
                curr = curr.next
            else:
                return head

        total = curr.data
        for _ in range(n - 1):
            if curr.next:
                curr = curr.next
                total += curr.data

        node = Node(total)
        temp = curr.next
        curr.next = node
        node.next = temp
        curr = temp
