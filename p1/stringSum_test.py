str_one = 'My'

str_two = 'Work'

str_sum = str_one + ' ' + str_two

print(str_sum)


def func_print(text):
    result = (f'my name is {text}')
    return result


name = 'Dima'
old = 25
print(f'Hello, {func_print(name)}, me is {old} old')

result_text = func_print(name) + ', me is ' + str(old) + ' old'
print(result_text)
