from callback_f_test1 import print_even_num
from callback_f_test1 import process_number

num = int(input('Enter youre number: '))
print_num = process_number(num, print_even_num)
print(print_num)
