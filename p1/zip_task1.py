list_subjects_name = ['juices', 'apples', 'flowers', 'books']
list_subjects_prices = ['100', '25', '50', '500']

zip_subjects = list(zip(list_subjects_name, list_subjects_prices))
print(zip_subjects)

set_subjects_test = set(zip_subjects)
print(set_subjects_test)

dict_subjects = dict(zip_subjects)
print(dict_subjects)

set_subjects = set(dict_subjects)
print(set_subjects)

set_subjects_copy = set_subjects
print(id(set_subjects), id(set_subjects_copy))
print(type(set_subjects_copy))