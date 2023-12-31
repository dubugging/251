def findMiddle(head):
    current = head
    length = 0
    while current:
        current = current.next
        length += 1
    for _ in range(length//2):
        head = head.next
    return head


def optimal(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
