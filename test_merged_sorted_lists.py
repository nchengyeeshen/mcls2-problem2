import unittest
from dataclasses import dataclass
from typing import List

from linked_list import to_linked_list, to_python_list
from merge_sorted_lists import merge_sorted_lists


@dataclass
class MergedSortedListsCase:
    """A merge_sorted_lists test case."""

    description: str
    l1: List
    l2: List
    expected: List


class TestMergedSortedLists(unittest.TestCase):
    def test_merging(self):
        cases = [
            MergedSortedListsCase("l1 is empty", [], [1, 2, 3], [1, 2, 3]),
            MergedSortedListsCase("l2 is empty", [1, 2, 3], [], [1, 2, 3]),
            MergedSortedListsCase(
                "l1 and l2 equal length", [1, 2, 3], [1, 2, 3], [1, 1, 2, 2, 3, 3]
            ),
            MergedSortedListsCase("l1 longer", [1, 2, 3, 4], [1], [1, 1, 2, 3, 4]),
            MergedSortedListsCase("l2 longer", [1], [1, 2, 3, 4], [1, 1, 2, 3, 4]),
        ]

        for case in cases:
            with self.subTest(msg=case.description):
                l1 = to_linked_list(case.l1)
                l2 = to_linked_list(case.l2)
                actual = to_python_list(merge_sorted_lists(l1, l2))
                self.assertEqual(actual, case.expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
