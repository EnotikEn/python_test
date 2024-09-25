list_number_one = [1, 50, 'string']
list_number_two = ['One', 45, 21]

list_sum = list_number_one + list_number_two
print(list_sum)

# operator + is using magic method __add__ for merge one list in other
list_test_sum = list_number_one.__add__(list_number_two)
print(list_test_sum)
