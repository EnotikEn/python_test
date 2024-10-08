number_one = 25


def print_number():
    number_one = 25
    print(id(number_one))

    def check_number(num):
        number_one = 'Check'
        print(number_one)
        return
    check_number(number_one)
    return number_one


print_number()
print(id(number_one))
