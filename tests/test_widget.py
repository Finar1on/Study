import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value, answer",
    [
        ("Maestro 1596837868705199", "1596 83** **** 5199"),
        ("Счет 64686473678894779589", "**9589"),
        ("Visa Classic 6831982476737658", "6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "8990 92** **** 5229"),
    ],
)
def test_mask_cardacc(value: str, answer: str) -> None:
    assert mask_account_card(value) == answer


@pytest.mark.parametrize("value", ["fgfasfas", "124512", "сочет 12345678901234567890"])
def test_mask_cardacc_exc(value: str) -> None:
    with pytest.raises(Exception):
        mask_account_card(value)


@pytest.mark.parametrize(
    "date, altered",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2025-07-06T01:45:02.512316", "06.07.2025"),
        ("2005-07-08T08:15:07.613632", "08.07.2005"),
    ],
)
def test_date(date: str, altered: str) -> None:
    assert get_date(date) == altered


@pytest.mark.parametrize("date", ["", "asfasgas", "2395723905723"])
def test_date_exc(date: str) -> None:
    with pytest.raises(Exception):
        get_date(date)
