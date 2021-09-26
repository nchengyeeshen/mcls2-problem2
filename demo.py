from random import randint

from linked_list import to_linked_list, to_python_list, Node
from merge_sorted_lists import merge_sorted_lists


def ll_repr(head: Node) -> str:
    """Return a string representation of a singly linked list"""
    return repr(to_python_list(head))


if __name__ == "__main__":
    print("-" * 72)
    print("Merge sorted lists demo")
    print("-" * 72)

    # Generate two sorted lists with integers in the interval [-10, 20]
    l1 = to_linked_list(list(range(randint(-10, 10), randint(10, 20), randint(1, 10))))
    l2 = to_linked_list(list(range(randint(-10, 10), randint(10, 20), randint(1, 10))))
    merged = merge_sorted_lists(l1, l2)

    print(f"List 1: {ll_repr(l1)}")
    print(f"List 2: {ll_repr(l2)}")
    print(f"Merged: {ll_repr(merged)}")
