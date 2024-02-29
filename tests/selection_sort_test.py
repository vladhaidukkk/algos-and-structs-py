from unittest.mock import patch

import pytest

from src.selection_sort import find_smallest, selection_sort


@pytest.mark.parametrize(
    "xs,expected",
    [
        ([3, 5, 1, 2, 4], 2),
        ([1, -2, 0, 2, -1], 1),
        ([2, 1, 4, 1, 3], 1),
    ],
)
def test_find_smallest(xs, expected):
    assert find_smallest(xs) == expected


def test_find_smallest_empty():
    with pytest.raises(
        ValueError, match=r"find_smallest\(\) iterable argument is empty"
    ):
        find_smallest([])


@pytest.mark.parametrize(
    "xs,expected",
    [
        ([3, 5, 1, 2, 4], [1, 2, 3, 4, 5]),
        ([3, 1, 3, 2, 4], [1, 2, 3, 3, 4]),
    ],
)
def test_selection_sort(xs, expected):
    assert selection_sort(xs) == expected


def test_selection_sort_immutability():
    xs = [3, 5, 1, 2, 4]
    xs_len = len(xs)
    selection_sort(xs)
    assert len(xs) == xs_len


@patch("src.selection_sort.find_smallest")
def test_selection_sort_calls_find_smallest(find_smallest_mock):
    find_smallest_mock.side_effect = find_smallest
    xs = [3, 5, 1, 2, 4]
    xs_len = len(xs)
    selection_sort(xs)
    assert find_smallest_mock.call_count == xs_len
