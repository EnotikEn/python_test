def print_even_num(num):
    if (num % 2) == 0:
        print('Number is even')
    else:
        print('Number isnt even')


def print_square_num(num):
    sum = num * num
    print(f'Square of number {num} is {sum}')


def process_number(num, callback):
    return callback(num)


input_value = int(input('Enter number: '))
process_number(input_value, print_even_num)
process_number(input_value, print_square_num)
