# Задание 1
def count_char_occurrences(text):
    result = {}
    for char in text.lower():
        if char.isalpha():
            result[char] = result.get(char, 0) + 1
    return result
pass
# Задание 2
def merge_dicts(dict1, dict2, conflict_resolver):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] = conflict_resolver(key, result[key], value)
        else:
            result[key] = value
    return result
pass
# Задание 3
def invert_dictionary(original_dict):
  inverted = {}
  for key, value in original_dict.items():
        inverted.setdefault(value, []).append(key)
  return inverted
pass
# Задание 4
def dict_to_table(data_dict, columns):
    if not data_dict:
        return ""

    col_widths = {
        'name': 6,
        'age': 5,
        'city': 8
    }
    
    header = "| " + " | ".join(
        col.upper().ljust(col_widths.get(col.lower(), len(col) + 2))
        for col in columns
    ) + " |"
    
    separator = "|" + "|".join(
        "-" * (col_widths.get(col.lower(), len(col) + 2)) 
        for col in columns
    ) + "|"

    rows = []
    for row_data in data_dict.values():
        row = []
        for col in columns:
            value = row_data.get(col, "N/A")
            if isinstance(value, (int, float)):
                value = str(value)
            width = col_widths.get(col.lower(), len(col) + 2)
            row.append(value.ljust(width))
        rows.append("| " + " | ".join(row) + " |")
    
    return "\n".join([header, separator] + rows)

pass
# Задание 5
def deep_update(base_dict, update_dict):
    for key, value in update_dict.items():
        if (key in base_dict and 
            isinstance(base_dict[key], dict) and 
            isinstance(value, dict)):
            deep_update(base_dict[key], value)
        elif key in base_dict:
            base_dict[key] = value
    return base_dict
pass