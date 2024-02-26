import pytest

from src.binary_search import binary_search


@pytest.mark.parametrize(
    "xs,target,expected",
    [
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 5, 4),
        ([1, 2, 3, 4, 5], 0, None),
        ([1, 2, 3, 4, 5], 6, None),
        ([], 1, None),
    ],
)
def test_binary_search_on_nums(xs, target, expected):
    assert binary_search(xs, target) == expected


@pytest.mark.parametrize(
    "xs,target,expected",
    [
        (["a", "b", "c", "d", "e"], "c", 2),
        (["a", "b", "c", "d", "e"], "a", 0),
        (["a", "b", "c", "d", "e"], "e", 4),
        (["a", "b", "c", "d", "e"], " ", None),
        (["a", "b", "c", "d", "e"], "f", None),
        ([], "a", None),
    ],
)
def test_binary_search_on_chars(xs, target, expected):
    assert binary_search(xs, target) == expected
