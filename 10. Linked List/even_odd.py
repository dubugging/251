def segregateOddEven(head):
    oddStart, oddEnd = None, None
    evenStart, evenEnd = None, None
    curr = head

    while curr:
        if curr.data % 2:
            if not oddStart:
                oddStart = curr
                oddEnd = curr
            else:
                oddEnd.next = curr
                oddEnd = oddEnd.next
        else:
            if not evenStart:
                evenStart = curr
                evenEnd = curr
            else:
                evenEnd.next = curr
                evenEnd = evenEnd.next
        curr = curr.next

    if oddStart and evenStart:
        oddEnd.next = evenStart
        evenEnd.next = None
        head = oddStart

    return head
