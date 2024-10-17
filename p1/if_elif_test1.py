num_one = int(input('Enter number one: '))
num_two = int(input('Enter number two: '))


def type_int(num_one, num_two):
    try:
        if (type(num_one) is not int):
            return print(f"{num_one} is not integer")
        elif (type(num_two) is not int):
            return print(f"{num_two} is not integer")
        else:
            return print('All numbers is integer')
    except Exception as e:
        print(e)


type_int(num_one, num_two)
