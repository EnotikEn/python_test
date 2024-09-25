set_values = {'1920x1080', '1600x900'}
set_values_new = {'800x600', '1920x1080'}

# all_values = set_values.union(set_values_new)
# or
all_values = set_values | set_values_new
print('First set add to second: ', all_values)

# general_elements = set_values.intersection(set_values_new)
# or
general_elements = set_values & set_values_new
print('General elements is ', general_elements)
