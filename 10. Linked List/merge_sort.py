class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __del__(self):
        if (self.next):
            del self.next


def get_mid(head):
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge(head1, head2):
    head = Node(-1)
    curr = head

    while head1 and head2:
        if head1.data < head2.data:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next

    while head1:
        curr.next = head1
        head1 = head1.next
        curr = curr.next

    while head2:
        curr.next = head2
        head2 = head2.next
        curr = curr.next

    return head.next


def sortLL(head):
    if not head.next:
        return head
    left = head
    mid = get_mid(head)
    right = mid.next
    mid.next = None
    return merge(sortLL(left), sortLL(right))
