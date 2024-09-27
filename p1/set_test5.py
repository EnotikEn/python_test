set_string = {'S', 'k', 'i', 'l', 'l'}

set_string.discard('l')
set_string.remove('S')

print(set_string)

set_string.add('Baby')

print(set_string)

set_other_string = {'my', 'd', 'r', 'l', 'k'}

print(set_string & set_other_string)

set_string_other = set_other_string.copy()
print(set_string_other)

print(set_string.symmetric_difference(set_other_string))
