def image_info(**dictionary):
    try:
        check_keys(dictionary)
    except Exception as e:
        print(e)
    else:
        return f"Image '{dictionary['image_title']}' has id {dictionary['image_id']}"


def check_keys(dictionary):
    image_title = 'image_title'
    image_id = 'image_id'
    if image_title not in dictionary:
        raise TypeError('ERROR: no key image_title')
        return dictionary[image_title]
    if image_id not in dictionary:
        raise TypeError('ERROR: no key image_id')
        return dictionary[image_id]


result_one = image_info(image_title='My_project', image_id=824365783425,
                        image_test='stirng_test')
print(result_one)

result_two = image_info(image_title='My_project', image_ida=824365783425)

print(result_two)

result_three = image_info(image_titles='My_project', image_id=824365783425)

print(result_three)
