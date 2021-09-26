from typing import Optional

from linked_list import Node


def merge_sorted_lists(l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
    """Merged two sorted singly linked lists into one linked list."""
    head = Node()
    node = head

    while l1 and l2:
        if l1.val < l2.val:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next
        node = node.next

    if l1:
        node.next = l1
    if l2:
        node.next = l2

    return head.next
