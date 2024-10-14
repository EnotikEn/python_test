dict_test = {
    'name': input('Enter your name: '),
    'info_text': input('Enter your welcome: '),
}


def welcome_info(name, info_text):
    if not info_text:
        info_text = 'Welcome'
        return print(f"{info_text} to site , {name}")
    return print(f"{info_text} to site , {name}")


welcome_info(**dict_test)

# or

welcome_info(dict_test['name'], dict_test['info_text'])

# or

welcome_info(name=dict_test['name'], info_text=dict_test['info_text'])
