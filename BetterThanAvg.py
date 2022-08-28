def better_than_average(class_points, your_points):
    average = 0
    for i in class_points:
        average = average + i
    average = average / len(class_points)
    if average < your_points:
        return True
    else:
        return False