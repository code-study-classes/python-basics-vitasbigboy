#Задача 1
def calculate_distance(x, y):
    return abs(x - y)

#Задача 2
def calculate_segments(a, b):
    return a // b

#Задача 3
def calculate_digit_sum(number):
    number = abs(number)
    return sum(int(digit) for digit in str(number))

#Задача 4
def calculate_rect_area(x1, y1, x2, y2):
    return abs(x2 - x1) * abs(y2 - y1)

#Задача 5
def round_to_multiple(number, multiple):
    return round(number / multiple) * multiple