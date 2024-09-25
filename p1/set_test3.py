set_numbers_first = {10, 5, 13}
set_numbers_second = {25, 16, 13, 55, 5, 20, 10}

set_numbers_ab = set_numbers_first.issubset(set_numbers_second)
set_numbers_ab_ab = set_numbers_second.issuperset(set_numbers_first)
print('First set included in the second: ', set_numbers_ab_ab)
print('Second set includes is first: ', set_numbers_ab)
