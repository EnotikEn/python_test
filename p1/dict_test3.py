my_disk = {}

print(id(my_disk))

print(type(my_disk))

my_disk['brand'] = 'Samsung'
my_disk['price'] = 900

print(my_disk)
print('___')
print(my_disk.items())
print(type(my_disk.items()))
print('___')
print(my_disk.keys())
print(type(my_disk.keys()))

# output == print(list(my_disk))
print(list(my_disk.keys()))

print('___')
# best using is oprator del
print('Delete last element in dict: ', my_disk.popitem())
print(my_disk)

new_disk = my_disk.copy()

new_disk['type'] = 'ssd'
print(new_disk)

keys = type(my_disk.keys())
print(keys)
