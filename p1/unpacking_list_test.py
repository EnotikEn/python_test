list_test = ['name', 'color']


def color_name(name, color):
    return print(f'Your {name} is {color}')


color_name(*list_test)

# or

name_g, color_g = list_test
color_name(name_g, color_g)
