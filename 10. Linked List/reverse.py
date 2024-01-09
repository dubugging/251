def reverseLinkedList(head):
	previous = None
	while head:
		after = head.next
		head.next = previous
		previous = head
		head = after
	return previous
