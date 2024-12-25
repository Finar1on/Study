from src import masks


def mask_account_card(payment: str) -> str:
    """Function that uses masks to edit given string based on whether it is an account or a card"""
    number = []
    for i in payment:
        if i.isdigit():
            number.append(str(i))
    if "счет" in payment.lower():
        return masks.get_mask_account("".join(str(e) for e in number))
    else:
        return masks.get_mask_card_number("".join(str(e) for e in number))


def get_date(date: str) -> str:
    """Function that edits the date format"""
    if date.isalpha() or len(date) > 26 or len(date) < 26:
        raise Exception("Incorrect date")
    else:
        return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
