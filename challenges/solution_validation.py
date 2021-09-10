def validate(codestring):
    if "def" not in codestring:
        return "missing def"
    elif ":" not in codestring:
        return "missing :"
    elif ("(" and ")") not in codestring:
        return "missing paren"
    elif ("(" + ")") in codestring:
        return "missing param"
    elif "    " not in codestring:
        return "missing indent"
    elif "validate" not in codestring:
        return "wrong name"
    elif "return" not in codestring:
        return "missing return"
    else:
        return True