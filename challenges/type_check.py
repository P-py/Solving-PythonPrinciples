def only_ints(x, y):
    typeX = type(x)
    typeY = type(y)
    
    if (typeX == int) and (typeY == int):
        return True
    else:
        return False