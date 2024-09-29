from copy import deepcopy

info = {
    'name': 'hello',
    'reviews': {
        'text': 'hi',
    }
}

info_deepcopy = deepcopy(info)

print(info_deepcopy.get('reviews'))
info_deepcopy['reviews']['text2'] = 'hello'
info['name'] = 'hi'

print(info)
print(info_deepcopy)
