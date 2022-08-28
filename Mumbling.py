def accum(s):
    string = ""
    index = 0
    for f in s:
        string = string + f.upper() + f.lower() * index + "-"
        index += 1
    return string[:-1]