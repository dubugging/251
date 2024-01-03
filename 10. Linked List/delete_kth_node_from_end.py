def removeKthNode(head, k):
    curr = head
    length = 0

    while curr:
        length += 1
        curr = curr.next

    curr = head
    k = length-k

    if k:
        for _ in range(1, k):
            curr = curr.next
        curr.next = curr.next.next
    else:
        head = head.next

    return head


def optimal(head, k):
    fast = head
    for _ in range(k):
        fast = fast.next

    if not fast:
        head = head.next
    else:
        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
    return head
