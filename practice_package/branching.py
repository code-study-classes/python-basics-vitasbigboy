# Задание 1
def is_weekend(day):
    return day in (6, 7)
pass
# Задание 2
def get_discount(amount):
    if amount >= 5000:
        return round(amount * 0.10, 2)
    elif amount >= 1000:
        return round(amount * 0.05, 2)
    else:
        return 0
pass
# Задание 3
def describe_number(n):
    if n % 2 == 0:
        parity = "четное"
    else:
        parity = "нечетное"

    if n < 10:
        digits = "однозначное"
    elif n < 100:
        digits = "двузначное"
    else:
        digits = "трехзначное"

    return f"{parity} {digits} число"
pass
# Задание 4
def convert_to_meters(unitNumber, lengthInUnits):
    conversion = {
        1: 0.1,
        2: 1000,
        3: 1,
        4: 0.001,
        5: 0.01
    }

    return lengthInUnits * conversion.get(unitNumber, 0)
pass
# Задание 5
def describe_age(age):
     ones = {
        1: "один", 2: "два", 3: "три", 4: "четыре",
        5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять"
    }

     tens = {
        2: "двадцать", 3: "тридцать", 4: "сорок",
        5: "пятьдесят", 6: "шестьдесят", 7: "семьдесят",
        8: "восемьдесят", 9: "девяносто", 10: "сто"
    }

     teens = {
        10: "десять", 11: "одиннадцать", 12: "двенадцать",
        13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать",
        16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать",
        19: "девятнадцать"
    }

     if 10 <= age % 100 <= 19:
        age_word = teens[age % 100]
     else:
        ten = age // 10
        one = age % 10
        age_word = tens.get(ten, "")
        if one:
            age_word += f" {ones[one]}"

     last_digit = age % 10
     last_two = age % 100
     if 11 <= last_two <= 14:
        suffix = "лет"
     elif last_digit == 1:
        suffix = "год"
     elif 2 <= last_digit <= 4:
        suffix = "года"
     else:
        suffix = "лет"

     return f"{age_word.strip()} {suffix}"
pass