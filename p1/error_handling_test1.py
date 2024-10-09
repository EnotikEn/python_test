try:
    print(10 + '5')
except Exception as e:
    print(e)
except TypeError as e:
    print(e)


print('Continue')


def error_f_division(one, two):
    if two == 0:
        raise ValueError('ERROR: Second value for argument is 0')
    return one / two


try:
    error_f_division(10, 0)
except Exception as e:
    print(e)
