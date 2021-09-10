def add_dots(sample):
    return '.'.join(sample)
    
def remove_dots(sample):
    sample = list(sample)
    new_sample = []
    for element in sample:
        if element != '.':
            new_sample.append(element)
        else:
            pass
    return ''.join(new_sample)
    