list_test_one = ['one', 'two', 'three', 'fourth']

del list_test_one[1]

list_test_one.__delitem__(2)

print(list_test_one)

dict_test = {
    'one': 'key',
    'two': 'key_test',
    'three': 'key_j',
}

dict_test.__delitem__('one')

print(dict_test)

del dict_test['two']

print(dict_test)
