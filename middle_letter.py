import math

def mid(string):
    string = list(string)
    if len(string)%2 == 0:
        return ""
    else:
        index = math.trunc(len(string)/2)
    return string[index]