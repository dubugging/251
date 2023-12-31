def get_mid(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    if head1.data > head2.data:
        head1, head2 = head2, head1
    ans = head1
    while head1 and head2:
        temp = None


def sort(head):
    if not head.next:
        return head
    left = head
    mid = get_mid(head)
    right = mid.next
    mid.next = None
    return merge(sort(left), sort(right))
