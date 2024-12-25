import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_mask_card(card_number: str) -> None:
    assert get_mask_card_number(card_number) == "1234 56** **** 3456"


def test_mask_account(account_number: str) -> None:
    assert get_mask_account(account_number) == "**7890"


@pytest.mark.parametrize("number", ["1", "123456789012345", "fasfagsdfgsaf", "fgasgfasg", ""])
def test_mask_account_exceptions(number: str) -> None:
    with pytest.raises(Exception):
        get_mask_account(number)


@pytest.mark.parametrize("number", ["1", "1234567890", "asfasf", "qwertyuiopqwerty", ""])
def test_mask_card_exceptions(number: str) -> None:
    with pytest.raises(Exception):
        get_mask_card_number(number)
