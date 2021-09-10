def is_anagram(string1, string2):
    string1 = list(string1)
    string2 = list(string2)
    string1.sort()
    string2.sort()
    if string1 == string2:
        return True
    else:
        return False