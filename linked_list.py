from typing import Optional, TypeVar

T = TypeVar("T")


class Node:
    def __init__(self, val: Optional[T] = None, next: Optional["Node"] = None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)


def to_linked_list(lst: list) -> Node:
    """Convert a Python list to a singly linked list."""
    head = Node()
    node = head

    for item in lst:
        node.next = Node(val=item)
        node = node.next

    return head.next


def to_python_list(head: Node) -> list:
    """Convert a singly linked list to a Python list."""
    lst = []

    while head:
        lst.append(head.val)
        head = head.next

    return lst
