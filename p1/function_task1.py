def merge_lists_to_dict(list_x, list_y):
    return dict(zip(list_x, list_y))


list_one = ['name', 'age', 'number', 'test']
list_two = ['user', 25, 777, 'test_login']

print(merge_lists_to_dict(list_one, list_two))
