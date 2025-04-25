# Задача 1
def sum_even_digits(number):
    number = abs(number)
    total = 0
    for digit in str(number):
        d = int(digit)
        if d % 2 == 0:
            total += d
    return total
pass
# Задача 2
def count_vowel_triplets(text):
     vowels = "aeiouy"
     text = text.lower()
     count = 0
     for i in range(len(text) - 2):
        if text[i] in vowels and text[i+1] in vowels and text[i+2] in vowels:
            count += 1
     return count
pass
# Задача 3
def find_fibonacci_index(number):
    if number == 1:
        return 1  # 1 is at both index 1 and 2
    a, b = 1, 1
    index = 2
    while b < number:
        a, b = b, a + b
        index += 1
    return index if b == number else -1
pass
# Задача 4
def remove_duplicates(string):
    if not string:
        return ""
    result = [string[0]]
    for char in string[1:]:
        if char != result[-1]:
            result.append(char)
    return ''.join(result)
pass