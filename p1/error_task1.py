def image_info(**dictionary):
    return f"Image '{dictionary['image_title']}' has id {dictionary['image_id']}"


def check_keys(**dictionary):
    set_keys = set(dictionary.keys())
    try:
        if set_keys != {'image_id', 'image_title'}:
            raise TypeError('ERROR: Not 2 args in keys')
    except Exception as e:
        print(e)
    else:
        result = image_info(dictionary)
        return result


print(image_info(image_title='str', image_id=1234))
