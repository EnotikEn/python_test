dict_main = {
    'name': 'Dmitry',
    'uid': 2345678
}

dict_main_mirror = dict_main
print(dict_main['name'], dict_main_mirror['name'])

dict_main_mirror['age'] = 25
print(dict_main['age'], dict_main_mirror['age'])

dict_main_copy = dict_main.copy()
dict_main_copy['new_atribute'] = 'new'
print(dict_main, dict_main_copy)


