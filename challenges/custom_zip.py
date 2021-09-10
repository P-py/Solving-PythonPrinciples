def zap(a, b):
    new_list = []
    for x in range(len(a)):
        new_list.append((a[x], b[x]))
    return new_list