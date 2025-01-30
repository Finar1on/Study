def filter_by_currency(transactions: list, curr: str = "USD") -> iter:
    """Function that sorts out wrong currency types"""
    filtered_list = []
    for i in transactions:
        if i["operationAmount"]["currency"]["name"] == curr:
            filtered_list.append(i)
    if not filtered_list:
        raise Exception("No corresponding transactions")
    else:
        return iter(filtered_list)


def transaction_descriptions(transactions: list) -> iter:
    """Function that only shows descriptions"""
    for i in transactions:
        yield i["description"]


def card_number_generator(start: int, end: int) -> iter:
    """Function that generates new card numbers"""
    for i in range(start, end + 1):
        new_number = "{:016d}".format(i)
        yield " ".join([new_number[o : o + 4] for o in range(0, len(new_number), 4)])
