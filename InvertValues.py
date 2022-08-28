def invert(lst):
    abs_num = 0
    abs_list = []
    for num in lst:
        if num < 0:
            abs_num = abs(num) 
            abs_list.append(abs_num)
        else:
            abs_num = 0 - num
            abs_list.append(abs_num)
    return abs_list