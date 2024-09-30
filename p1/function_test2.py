def func_of_change_atribute(x_dict):
    x_dict['id'] = x_dict['number'] + 10
    return x_dict


dict_num = {
    'name': 'User',
    'number': 57,
}

print(func_of_change_atribute(dict_num))
