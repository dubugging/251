def pairsSwap(head):
    if not head or not head.next:
        return head
        
    second = head.next
    third = head.next.next
    second.next = head
    head.next = pairsSwap(third)
    return second
