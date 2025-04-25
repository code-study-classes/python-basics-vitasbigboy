#Задача 1
def check_between_numbers(A, B, C):
    return (A < B < C) or (C < B < A)
pass
# Задача 2
def check_odd_three(number):
    return (100 <= abs(number) <= 999) and (number % 2 != 0)
pass
#Задача 3
def check_unique_digits(number):
    if not (100 <= abs(number) <= 999):
     return False
    digits = str(abs(number))
    return len(set(digits)) == 3
pass
#Задача 4
def check_palindrome_number(number):
    num_str = str(abs(number))
    return num_str == num_str[::-1]
pass
#Задача 5
def check_ascending_digits(number):
    if not (100 <= abs(number) <= 999):
        return False

    digits = [int(d) for d in str(abs(number))]

    return digits[0] < digits[1] < digits[2]
pass