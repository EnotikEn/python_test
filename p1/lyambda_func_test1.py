def function_test(text):
    return lambda name: f'{name} is {text}'


text_one = function_test('Good')

print(text_one('Dima'))

text_two = function_test('Bad')

print(text_two('Sasha'))
