import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_proc(dictgen: list) -> None:
    assert next(filter_by_currency(dictgen)) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


def test_desc(dictgen: list) -> None:
    assert next(transaction_descriptions(dictgen)) == "Перевод организации"


@pytest.mark.parametrize("st, fn, res", [(1, 10, 1), (5, 20, 5), (0, 0, 0), (2, 15, 2)])
def test_card_num(st: int, fn: int, res: int) -> None:
    assert int((next(card_number_generator(st, fn)))[18]) == res


def test_card_ran() -> None:
    a = card_number_generator(1, 9)
    results = []
    expected_results = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        results.append(int(next(a)[18]))
    assert results == expected_results


def test_card_err() -> None:
    with pytest.raises(Exception):
        a = card_number_generator(1, 10)
        for i in range(12):
            print(next(a))
