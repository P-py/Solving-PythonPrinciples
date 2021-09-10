def all_equal(list1):
    set_comparasion = set(list1)
    if len(set_comparasion) == 1 or len(set_comparasion) == 0:
        return True
    else:
        return False