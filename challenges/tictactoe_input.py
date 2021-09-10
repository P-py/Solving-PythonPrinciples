from collections import namedtuple

def get_row_col(text):
    text = list(text)
    convert = []
    row = text[1]
    column = text[0]
    
    if row == "1":
        convert.append(0)
    elif row == "2":
        convert.append(1)
    elif row == "3":
        convert.append(2)

    if column == "A":
        convert.append(0)
    elif column == "B":
        convert.append(1)
    elif column == "C":
        convert.append(2)
            
    convert = tuple(convert)
    return convert