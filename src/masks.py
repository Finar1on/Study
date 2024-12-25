def get_mask_card_number(number: str) -> str:
    """Function that converts given number into an appropriate format"""
    if len(number) > 16 or len(number) < 16 or number.isalpha():
        raise Exception("Incorrect number")
    else:
        mask = number[0:4] + " " + number[4:6] + "**" + " ****" + " " + number[12:]
        return mask


def get_mask_account(accnum: str) -> str:
    """Function that converts given account number into an appropriate format"""
    if len(accnum) > 20 or len(accnum) < 20 or accnum.isalpha():
        raise Exception("Incorrect number")
    else:
        accmask = "**" + accnum[16:21]
        return accmask
