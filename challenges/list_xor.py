def list_xor(n, list1, list2):
    if (n in list1) and (n in list2):
        return False
    elif (n not in list1) and (n not in list2):
        return False
    else:
        return True 