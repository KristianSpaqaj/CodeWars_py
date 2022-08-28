def solution(string, ending):
    length = len(ending)
    if ending == string[-length:] or ending == "":
        return True
    else:
        return False