def count_sheep(n):
    string = ""
    for f in range(1,n+1):
        string = string + f"{f} sheep..."
    return string
#Old version
def count_sheep2(n):
    string = ""
    for f in range(n+1):
        if f == 0:
            continue
        string = string + f"{f} sheep..."
    return string