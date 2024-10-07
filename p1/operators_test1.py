dict_one = {
    'width': 200,
    'length': 100,
}

other_dict = {
    **dict_one,
    'text': 'Hello, friend',
    'width': 150,
}

dict_sum = dict_one | other_dict

print(dict_sum)