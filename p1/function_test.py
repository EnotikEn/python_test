def func_test():
    return print('Hello , World')


def func_id_num(a, b):
    print(id(a))
    a += 1
    print(id(a))
    c = a + b
    return c


func_test()

a_num = 10
print(id(a_num))
b_num = 5
func_id_num(a_num, b_num)
