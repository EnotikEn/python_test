# # name = 'Dima'


# # def my_name(name):
# #     print(name)
# #     return 0


# # print(name)  # Comment

# def sum_nums(a, b):
#     sum = a + b
#     return sum


# first_num = 1423
# second_num = 1488

# sum_fas_nums = sum_nums(first_num, second_num)

# print(sum_fas_nums)

# print(sum_nums(sum_nums(first_num, second_num), 100))


# print(input('Dima'))

# name = input('Enter Your name: ')


def name_f(name):
    # print('Your name is:', name)
    return 'Welcome', name


# print(name_f(name))

# print(id(name_f))
# print(type(name_f))

CONST_LOG = 'D_Oleynikov'
CONST_PORT = 3389


def output_def_name(login):
    print(login)
    return login


int_number = 234
float_number = 12.4
bool_value = True

# print(int_number + float_number)
# print(float_number + int_number)

# print(int_number + bool_value)
# print(bool_value + int_number)


# print(bool_value + float_number)

# print(CONST_LOG * float_number)

# print(dir(bool))


# print(help(print()))

cars_list = ['Bugatti', 'VAZ', 'Skoda', 'Mercedes-Benz', 'SSC']
# cars_no_random_list = ['VAZ', 'Bugatti', 'Mercedes-Benz', 'Skoda']
# cars_duplicate_list = ['VAZ', 'Bugatti', 'Mercedes-Benz', 'Skoda']

# print(cars_list == cars_no_random_list)

# print(cars_no_random_list == cars_duplicate_list)

# print('Thank you for watching')

# print(len(cars_list))

# print(len(CONST_LOG))

# print(CONST_LOG[3])
# print(cars_list[2])

# print(cars_list)

# del cars_list[4]
# print(cars_list)

# del cars_list[-1]

# print(cars_list)


# def func_test(a, b):
#     x = 10
#     y = 15
#     z = x + y
#     return z


# print(func_test(10, 15))

# users = [
#     {
#         'user_id': 0,
#         'user_name': 'D_Oleynikov'
#     },
#     {
#         'user_id': 1,
#         'user_name': 'D_Oleynikov8'
#     },
#     {
#         'user_id': '2',
#         'user_name': 'Admin'
#     }
# ]

# # print(len(users))

# print(users)

# # print(users[2]['user_name'])

# new_dict_for_users = {
#     'user_id': int(input('Enter your id: ')),
#     'user_name': input('Enter your name: ')
# }

# users.append(new_list_for_users)

# print(users)

# print('(Comment) I add last list of list ''Users'':''', new_list_for_users)

# removed_list_for_users = users.pop()

# print(users)

# print('(Comment) I remove last list of list ''Users'':''', removed_list_for_users)

# string_for_list = 'HOC'

# list_from_string = list(string_for_list)

# print(list_from_string)

# list_from_dict = list(new_dict_for_users)

# print(list_from_dict)

# ratings = [float(input('1 value: ')), float(input('2 value: ')),
#            float(input('3 value: ')), float(input('4 value: '))]

# print('Current rating', ratings)

# print('Min value ratings', min(ratings))
# print('Max values rating', max(ratings))

# print('Average value rating', max(ratings)/len(ratings))

# ratings_other = [4.6, 5.0, 2.3, 3.1, 2.7, 3.3]

# all_sum_retings = ratings + ratings_other

# # print(all_sum_retings)

# my_num = [10, 34, 10, 65]

# print(type(my_num))
# print(dir(my_num))

# count_res = my_num.count(10)

# print(count_res)

# my_num.append(110)
# print(my_num)

# my_num.clear()

# print(my_num)
