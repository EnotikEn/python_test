my_room = {
    'table': 'GamingPRO',
    'bed': 'SpaceIterprises',
    'locker': 'Digger',
    'price': 25000,
    'volume_bass': 148.8,
    'bypass': 1,
    'new_dict': {
        'new_value': 'Hello, World!',
        'old_value': 'Hi, Kitty',
    }
}

print(my_room['volume_bass'])

my_room['price'] = 35000

print('Added new value in dictionary: ', my_room['price'])

my_test_room = {
    'table': 'GamingPRO',
    'bed': 'SpaceIterprises',
    'locker': 'Digger',
    'price': 35000,
    'volume_bass': 148.8,
}

print(my_room == my_test_room)

my_room['new_volume'] = 'Degeneration'

print(my_room)

del my_room['new_volume']

print(my_room)

key_prop_dict = 'bypass'

my_room[key_prop_dict] = 999

print(my_room)

print(my_room['new_dict']['new_value'])
print(my_room['new_dict']['old_value'])
