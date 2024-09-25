date = '01.12.2024'
user = 'root'
balance = 6778

dict_office = {
    'date': date,
    'user': user,
    'balance': balance,
    'other_dict': {
        'hell': 'man',
        'hall': 'girl',
    }
}

print(dict_office)

print(len(dict_office))

print(dict_office.get('value', 'Not given key'))

print('_#_#_#_')

list_office = [
    'marry_k', 'given_k', '345_k'
]

list_office_two = [
    'marrys', 'givens', 3456
]
new_dict_office = dict(zip(list_office, list_office_two))

print(new_dict_office)

print('___')

list_office1 = list(dict_office.keys())
print(list_office1)

# print('___')
# list_office1 = dict(list_office1)
