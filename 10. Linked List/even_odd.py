def segregateOddEven(head):
    es, ee = None, None
    os, oe = None, None
    curr = head
    while curr:
        data = curr.data
        if data % 2:
            if not os:
                os = curr
                oe = curr
            else:
                oe.next = curr
                oe = oe.next
        else:
            if not es:
                es = curr
                ee = curr
            else:
                ee.next = curr
                ee = ee.next
        curr = curr.next

    if not os:
        return es
    elif not es:
        return os
    else:
        oe.next = es
        return os
