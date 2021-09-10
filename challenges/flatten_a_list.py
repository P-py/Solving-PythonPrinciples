def flatten(x):
    returning = []
    for elements in x:
        for element in elements:
            returning.append(element)
    return returning