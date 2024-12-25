import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("state", ["EXECUTED", "CANCELED"])
def test_filter_state(filter_state: list, state: str) -> None:
    for i in filter_by_state(filter_state, state):
        assert i["state"] == state


@pytest.mark.parametrize("sort_method, key_word", [(True, "newold"), (False, "oldew")])
def test_sort_d(sort_method: bool, compiled: dict, key_word: slice, filter_state: list) -> None:
    assert sort_by_date(filter_state, sort_method) == compiled[key_word]


@pytest.mark.parametrize("sort_method, key_word", [(False, "newold"), (True, "oldew"), (True, [])])
def test_sort_d_exc(sort_method: bool, compiled: str, key_word: slice, filter_state: list) -> None:
    with pytest.raises(Exception):
        assert sort_by_date(filter_state, sort_method) == compiled[key_word]
