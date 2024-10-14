list_dict_values = [
    {
        'room_1': 'bathroom',
        'room_2': 'kitchen',
    },
    {
        'car_1': 'LADA',
        'car_2': 'BMW',
    },
    {
        'name_1': 'Ivan',
        'name_2': 'Varvara',
    },
]

dict_room_names, *other_names = list_dict_values

# print('Dictionary room names: ', dict_room_names)
# print('Dictionary car names: ', dict_car_names)
# print('Dictionary people names: ', dict_people_names)


def add_value_names(value, name):
    print('key:values - ', value, name)


add_value_names(dict_room_names, other_names)
