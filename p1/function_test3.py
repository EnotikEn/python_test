def f_work_with_dict(x_dict):
    x_dict_cp = x_dict.copy()
    x_dict_cp['numbers'] = 777
    return x_dict_cp


dict_main = {
    'name': 'Bazooka',
    'numbers': 999,
}

print('original dict: ', dict_main, '| copy dict: ', f_work_with_dict(dict_main))
