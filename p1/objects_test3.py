dict_test = {
    'name': 1,
    'comments': {
        1: 'q',
        2: 'x',
    }
}

dict_test_shallow_copy = dict_test.copy()
del dict_test_shallow_copy['comments'][2]
dict_test['name'] = 2
print(dict_test)
print(dict_test_shallow_copy)



