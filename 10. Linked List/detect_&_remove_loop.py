class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def detect_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
    return None


def removeLoop(head: Node) -> Node:
    meet = detect_cycle(head)
    if not meet:
        return head
    start = head
    previous = None
    while start != meet:
        previous = meet
        start = start.next
        meet = meet.next
        if start == meet:
            previous.next = None
            return head
