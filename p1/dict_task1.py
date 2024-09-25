dict_auto = {}

key_1 = input('Enter 1 key: ')

key_2 = input('Enter 2 key: ')

key_3 = input('Enter 3 key: ')


dict_auto[key_1] = input('Enter 1 value for 1 key: ')

dict_auto[key_2] = input('Enter 2 value for 2 key: ')

dict_auto[key_3] = input('Enter 3 value for 3 key: ')

print(dict_auto)

dict_auto['k4'] = 'v4'

print(dict_auto)

del dict_auto['k4']

print(dict_auto)
