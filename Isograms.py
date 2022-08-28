def is_isogram(string):
    test = ""
    for f in string.lower():
        if f in test:
            return False
        else:
            test = test + f
    return True
        