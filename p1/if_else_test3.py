def num_int(num_one, num_two):
    if (type(num_one) is not int) and (type(num_two) is not int):
        return 'First or Second number is not integer'
    elif num_one > num_two:
        return f"{num_one} > {num_two}"
    else:
        return f"{num_one} < {num_two}"


print(num_int(56, 100))
