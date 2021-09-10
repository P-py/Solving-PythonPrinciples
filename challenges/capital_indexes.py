def capital_indexes(string):
    list = enumerate(string)
    capital = []
    for count, item in list:
        if item.isupper():
            capital.append(count)
    return capital