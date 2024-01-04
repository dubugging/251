def pairsSwap(head):
    if not head or not head.next:
        return head
    new_head = head.next
    third = head.next.next
    new_head.next = head
    head.next = pairsSwap(third)
    return new_head
