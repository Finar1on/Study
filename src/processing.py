def filter_by_state(array: list, state: str = "EXECUTED") -> list:
    """Function that filters out dictionaries with unwanted state"""
    arrnew = []
    for i in array:
        if state in i["state"]:
            arrnew.append(i)
    return arrnew


# Had to write it like this because reverse didn't let me refer to a variable 'order'
def sort_by_date(farray: list, order: bool = True) -> list:
    """Function that sorts previously filtered list by date"""
    if order:
        return sorted(farray, key=lambda x: x["date"], reverse=True)
    else:
        return sorted(farray, key=lambda x: x["date"], reverse=False)
