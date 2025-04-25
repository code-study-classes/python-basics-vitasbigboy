# Задание 1
def find_common_elements(set1, set2):
  return set1 & set2
pass
# Задание 2
def is_superset(set_a, set_b):
  return set_a.issuperset(set_b)
pass
# Задание 3
def remove_duplicates(items):
  seen = set()
  return [x for x in items if not (x in seen or seen.add(x))]
pass
# Задание 4
def count_unique_words(text):
  words = text.lower().split()
  return len(set(words)) if text else 0
pass
# Задание 5
def find_shared_items(*sets):
  if not sets:
    return set()
  return set.intersection(*sets)
pass