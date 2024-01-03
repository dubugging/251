class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def addTwoNumbers(head1: Node, head2: Node) -> Node:
    head = Node(-1)
    curr = head
    carry = 0
    while head1 or head2 or carry:
        sum = 0
        if head1:
            sum += head1.data
            head1 = head1.next
        if head2:
            sum += head2.data
            head2 = head2.next

        sum += carry
        carry = sum//10

        temp = Node(sum % 10)
        curr.next = temp
        curr = curr.next

    return head.next
