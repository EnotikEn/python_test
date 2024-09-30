def func_test(num_x, num_y):
    sum = num_x + num_y
    return sum

num_one = 10
num_two = 20
num_three = 30
# print(func_test(num_one, num_two))

def arg_tuple(*args):
    print(args)
    print(type(args))
    # print(args[0])
    return sum(args)

# print(arg_tuple(12, 23, 56, 99, 12))
print(arg_tuple())