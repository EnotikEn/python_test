set_numbers = {34, 134, 734}

set_numbers.add(934)

set_other_numbers = {77, 34, 99, 134}

set_general_numbers = set_numbers & set_other_numbers
print('Outputting general elements of 2 sets: ', set_general_numbers)

set_in_list_general = list(set_general_numbers)
print('List from set: ', set_in_list_general)

set_union_numbers = set_numbers | set_other_numbers
print('Outputting union sets: ', set_union_numbers)

set_diff_numbers = set_numbers - set_other_numbers
print('Outputting diffrence between 2 sets: ', set_diff_numbers)

list_diff_numbers = list(set_diff_numbers)
print('list from set: ', list_diff_numbers)

print(set_numbers, '|', set_other_numbers)

del set_numbers[2]
