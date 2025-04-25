#Задача 1
def extract_file_name(full_file_name):
    base = full_file_name.split('/')[-1]
    if base.startswith('.'):
        base = base[1:]
    return base.split('.')[0]

#Задача 2
def encrypt_sentence(sentence):
    even = sentence[1::2]
    odd = sentence[0::2][::-1]
    return even + odd

#Задача 3
def check_brackets(expression):
    balance = 0
    for i, char in enumerate(expression):
        if char == '(':
            balance += 1
        elif char == ')':
            if balance == 0:
                return i
            balance -= 1
    return -1 if balance > 0 else 0

#Задача 4
def reverse_domain(domain):
    parts = domain.split('.')
    return '.'.join(reversed(parts))

#Задача 5
def count_vowel_groups(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    word = word.lower()
    count = 0
    in_group = False
    for char in word:
        if char in vowels:
            if not in_group:
                count += 1
                in_group = True
        else:
            in_group = False
    return count