def route_info(dictionary):
    if ('distance' in dictionary) and (isinstance(dictionary.get('distance'), int)):
        return f"Distance to your destination is <{dictionary['distance']}>"
    elif ('speed' in dictionary) and ('time' in dictionary) and (isinstance(dictionary.get('speed'), int)) and (isinstance(dictionary.get('time'), int)):
        speed = dictionary['speed']
        time = dictionary['time']
        return f"Distance to your destination is {speed * time}"
    else:
        return 'No distance info is available'


def new_dict():
    input_dict = {}
    for i in range(3):
        key = input('Enter key: ')
        if (key == 'distance') or (key == 'speed') or (key == 'time'):
            value = int(input('Enter value is integer: '))
            input_dict[key] = value
        else:
            value = input('Enter value: ')
            input_dict[key] = value
    return input_dict


dictionary = new_dict()
print(route_info(dictionary))
